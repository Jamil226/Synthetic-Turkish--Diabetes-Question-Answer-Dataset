# Sentetik Türkçe Diyabet Soru-Cevap Veri Seti (100K)

## Genel Bakış

Bu depo, diyabet ve ilişkili kronik hastalıklar hakkında **100.000 sentetik Türkçe hasta soru-cevap kaydı** içerir. Veri seti, sağlık alanındaki büyük dil modellerinin (LLM) eğitimi, değerlendirilmesi ve Türkçe klinik diyalog sistemlerinin geliştirilmesi için hazırlanmıştır.

Tüm kayıtlar sentetiktir; gerçek hasta verisi içermez.

---

## Veri Seti Özeti

- **Dosya yolu:** `synthesized_100k.json`
- **Toplam kayıt:** 100.000 soru-cevap çifti
- **Dil:** Türkçe
- **Kapsam:** Tip 1 ve Tip 2 diyabet, gebelik diyabeti, metabolik sendrom, hipertansiyon, kardiyovasküler hastalıklar ve diğer kronik hastalıklar
- **Üretim betiği:** `ncd_generator_100k.py`

---

## Veri Yapısı

`synthesized_100k.json` dosyasındaki her kayıt aşağıdaki alanları içeren bir JSON nesnesidir:

```json
{
  "patient_query": "Tip 2 diyabet tanısı aldım. Beslenmemde nelere dikkat etmeliyim?",
  "doctor_response": "Kan şekeri kontrolü için düzenli öğünler planlayın, liften zengin besinleri tercih edin ve kişisel tedavi planınız için doktorunuza danışın.",
  "category": "Tip 2 Diyabet"
}
```

### Şema Açıklaması

- `patient_query` *(string)*: Hastanın diyabet, yaşam tarzı, ilaç kullanımı veya ilişkili klinik bir durum hakkındaki sorusu.
- `doctor_response` *(string)*: Hastaya yönelik, anlaşılır ve klinik açıdan yönlendirici yanıt.
- `category` *(string)*: Kaydın ait olduğu klinik kategori.

---

## Kullanım Alanları

- **Türkçe sağlık LLM'leri:** Diyabet ve kronik hastalık odaklı denetimli ince ayar (SFT) çalışmaları.
- **Klinik güvenilirlik değerlendirmesi:** Sağlık asistanlarının yanıt tutarlılığı ve klinik uygunluğunun ölçülmesi.
- **Dijital sağlık uygulamaları:** Türkçe hasta destek, tele-sağlık ve uzaktan izlem sistemleri için diyalog verisi.

---

## Lisans ve Sorumluluk Reddi

Veri setindeki tüm içerik sentetiktir ve akademik/klinik doğal dil işleme araştırmaları için hazırlanmıştır. Profesyonel tıbbi tavsiye, tanı veya tedavinin yerine geçmez.
