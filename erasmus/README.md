# FILS 2026/27 güz: Erasmus ders eşleştirme

- `data.py`: 24 TR dersinin içerik özeti, İngilizce karşılık adayları (güç 3/2/1) ve FILS ders/lab saatleri (tek/çift hafta dahil).
- AKTS: MSE değerleri fişlerden; lisans değerleri tahmini (`AKTS_TAHMIN`, sayfada düzenlenebilir). Toplam SPM dahil 30–40 AKTS.
- `solver.py`: SPM (Bitirme) sabit, Erasmus labı öncelikli, çakışmasız ve maksimal tüm programları `programs.json` dosyasına yazar.
- `build_report.py` + `template.html`: `rapor.html` (filtreli, haftalık ızgaralı rapor) üretir.

Yeniden üretmek için: `cd erasmus && python3 solver.py && python3 build_report.py`
