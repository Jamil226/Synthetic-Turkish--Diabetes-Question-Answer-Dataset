#!/usr/bin/env python3
"""
Filter and deduplicate question_bank/seed_data_10k.json to create
question_bank/seed_data_5k.json (exactly 5,000 diverse, non-duplicate Q&A pairs).

Deduplication & Selection Criteria:
1. Strict Uniqueness:
   - Zero exact duplicate queries.
   - Zero normalized duplicate queries (case-insensitive, whitespace collapsed, punctuation removed).
2. Clinical Scenario Coverage:
   - Retains 100% of all unique base medical scenarios (758/758) by prioritizing
     the concise primary clinical question (without suffix).
3. Proportional Distribution:
   - Matches the original dataset proportions across the 4 disease categories:
     - Cardiovascular Disease: 1,517 (30.34%)
     - Diabetes: 1,264 (25.28%)
     - Obesity: 1,133 (22.66%)
     - Hypertension: 1,086 (21.72%)
4. Diversity:
   - Round-robin selection of diverse follow-up variations across all base scenarios.
"""

import json
import re
import string
from collections import defaultdict, Counter
from pathlib import Path


def clean_query(text: str) -> str:
    """Normalize text by lowercasing, stripping punctuation, and collapsing whitespace."""
    trans = str.maketrans('', '', string.punctuation)
    return re.sub(r'\s+', ' ', text.lower().strip().translate(trans))


def get_base_scenario(query: str) -> str:
    """Extract root question before the '? Also,' suffix."""
    parts = re.split(r'\?\s+Also,', query)
    return parts[0] + '?' if len(parts) > 1 else query


def main():
    repo_dir = Path(__file__).resolve().parent
    input_file = repo_dir / "question_bank" / "seed_data_10k.json"
    output_file = repo_dir / "question_bank" / "seed_data_5k.json"

    print(f"Loading input file: {input_file}")
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"Loaded {len(data):,} records from {input_file.name}")

    # Step 1: Remove exact and normalized duplicates
    seen_clean = set()
    deduped_data = []
    removed_duplicates = 0

    for item in data:
        cleaned = clean_query(item["patient_query"])
        if cleaned not in seen_clean:
            seen_clean.add(cleaned)
            deduped_data.append(item)
        else:
            removed_duplicates += 1

    print(f"Removed {removed_duplicates} near-duplicate queries; {len(deduped_data):,} remain.")

    # Target counts matching proportional distribution to reach exactly 5,000
    targets = {
        "cardiovascular disease": 1517,
        "diabetes": 1264,
        "obesity": 1133,
        "hypertension": 1086,
    }
    target_total = sum(targets.values())
    assert target_total == 5000, f"Expected 5000, got {target_total}"

    # Step 2: Group by category and base scenario
    cat_scenarios = defaultdict(lambda: defaultdict(list))
    for item in deduped_data:
        cat = item["category"]
        base = clean_query(get_base_scenario(item["patient_query"]))
        cat_scenarios[cat][base].append(item)

    selected_cleaned_keys = set()

    for cat, target in targets.items():
        scenarios = cat_scenarios[cat]
        scenario_keys = list(scenarios.keys())
        scenario_picks = {k: [] for k in scenario_keys}

        # Priority 1: Pick base question without '? Also,' first to ensure 100% scenario coverage
        for k in scenario_keys:
            items = scenarios[k]
            base_item = next(
                (it for it in items if "? Also," not in it["patient_query"]),
                items[0]
            )
            scenario_picks[k].append(base_item)

        current_count = len(scenario_keys)

        # Priority 2: Round-robin selection of diverse follow-up variations
        variation_pool = {
            k: [it for it in scenarios[k] if it != scenario_picks[k][0]]
            for k in scenario_keys
        }

        step = 0
        while current_count < target:
            added = 0
            for k in scenario_keys:
                if current_count >= target:
                    break
                if len(variation_pool[k]) > step:
                    scenario_picks[k].append(variation_pool[k][step])
                    current_count += 1
                    added += 1
            step += 1
            if added == 0:
                break

        for k in scenario_keys:
            for item in scenario_picks[k]:
                selected_cleaned_keys.add(clean_query(item["patient_query"]))

    # Step 3: Filter dataset preserving original order
    final_records = [
        item for item in deduped_data
        if clean_query(item["patient_query"]) in selected_cleaned_keys
    ]

    print("\nSelection Summary:")
    print(f"Total Selected: {len(final_records):,}")
    category_counts = Counter(r["category"] for r in final_records)
    for cat, count in category_counts.items():
        pct = (count / len(final_records)) * 100
        print(f"  - {cat:.<26} {count:>5,} ({pct:>5.2f}%)")

    # Step 4: Validate constraints
    assert len(final_records) == 5000, f"Expected 5000, got {len(final_records)}"
    assert len(set(r["patient_query"] for r in final_records)) == 5000, "Queries are not all unique!"
    assert len(set(clean_query(r["patient_query"]) for r in final_records)) == 5000, "Cleaned queries have collisions!"

    # Step 5: Save output file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(final_records, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully wrote 5,000 records to: {output_file}")


if __name__ == "__main__":
    main()
