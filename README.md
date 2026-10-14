# Clinical Diabetes Question-Answer Dataset (5K)

## Overview
This repository provides a curated, deduplicated dataset of 5,000 clinical question-answer pairs focused on Diabetes Mellitus and associated cardiometabolic conditions (including diabetic cardiovascular complications, hypertension, and obesity management). The dataset was developed and utilized for evaluating and fine-tuning Large Language Models (LLMs) in Internet of Medical Things (IoMT) and smart healthcare environments.

This dataset is used in the following conference paper:
> **Parameter-Efficient Fine Tuning with QLoRA for Enhancing Clinical Reliability of LLMs in IoMT Applications**

---

## Dataset Summary

- **File Path**: `question_bank/seed_data_5k.json`
- **Total Records**: 5,000 question-answer pairs
- **Uniqueness**: 100% unique patient queries (verified via strict case-folding, whitespace collapsing, and punctuation-invariant normalization)
- **Clinical Scenario Coverage**: 758 foundational medical scenarios covering core patient queries and realistic situational follow-ups (e.g., blood glucose tracking, medication and insulin timing, acute hypoglycemia/hyperglycemia warning signs, dietary carb counting, foot care, and caregiver guidance)

### Category Distribution

| Category | Count | Percentage | Focus Area |
| :--- | :---: | :---: | :--- |
| **Cardiovascular Disease** | 1,517 | 30.34% | Diabetic heart health & macrovascular complications |
| **Diabetes** | 1,264 | 25.28% | Glycemic control, insulin management, and diet |
| **Obesity** | 1,133 | 22.66% | Weight management & metabolic risk reduction |
| **Hypertension** | 1,086 | 21.72% | Blood pressure control & vascular health |
| **Total** | **5,000** | **100.00%** | Comprehensive Diabetes & Cardiometabolic Care |

---

## Data Structure

Each record in `question_bank/seed_data_5k.json` is a JSON object with the following fields:

```json
{
  "patient_query": "I just found out I have Type 2 Diabetes. Is it true I can never eat bread or pasta again?",
  "doctor_response": "Not at all. You don't have to cut them out completely, but you should switch to whole-grain versions. They have more fiber, which slows down sugar absorption. Also, try the 'plate method': fill half your plate with non-starchy vegetables to balance the carbs.",
  "category": "diabetes"
}
```

### Schema Description
- `patient_query` *(string)*: Real-world patient question or clinical concern regarding diabetes diagnosis, daily glycemic management, lifestyle habits, or medication.
- `doctor_response` *(string)*: Clinically aligned, evidence-based physician response providing clear, actionable medical guidance.
- `category` *(string)*: Clinical domain (`diabetes`, `cardiovascular disease`, `hypertension`, `obesity`).

---

## Applications

- **Parameter-Efficient Fine-Tuning (PEFT / QLoRA)**: Supervised fine-tuning of open-source medical LLMs for diabetes self-management and IoMT edge devices.
- **Clinical Reliability & Safety Benchmarking**: Testing conversational consistency, clinical grounding, and hallucination reduction in digital diabetes health assistants.
- **IoMT & Telehealth Dialogue Systems**: Providing structured grounding data for patient-facing virtual diabetes care agents.

---

## Citation

If you use this dataset in your research, please cite our conference paper:

```bibtex
@inproceedings{jamil2026peft,
  title={Parameter-Efficient Fine Tuning with QLoRA for Enhancing Clinical Reliability of LLMs in IoMT Applications},
  author={Jamil, Muhammad},
  year={2026}
}
```

---

## License & Disclaimer
All data is synthetic and curated for academic and clinical NLP research purposes. It is not intended as a substitute for professional medical advice, diagnosis, or treatment.
