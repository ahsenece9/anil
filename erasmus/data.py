"""Ders verileri: TR dersleri, FILS (UPB) İngilizce dersleri, oturum saatleri ve içerik eşleşmeleri.

Saat gösterimi: (gün, başlangıç, bitiş, hafta)
  gün   : Pzt, Sal, Çar, Per, Cum
  hafta : "H" her hafta, "T" tek (odd) hafta, "Ç" çift (even) hafta
Kaynak: MSE-2026-2027-sem1.pdf (yüksek lisans SE) ve FILS-Engl-2026-2027_sem-1.pdf (lisans 1-4).
Diyagonal bölünmüş hücrelerde üst kısım = tek hafta, alt kısım = çift hafta.
"""

# ---------------------------------------------------------------------------
# İngilizce dersler. "C" = derse her durumda girilir (ders/kurs saatleri).
# "lab" = alternatif lab/proje/seminer seçenekleri; bir tanesi seçilir.
# Erasmus'a ayrılmış lab varsa yalnızca o seçenek konur (kullanıcı tercihi).
# ---------------------------------------------------------------------------
EN = {
    "SPM": dict(
        ad="Software Project Management", prog="MSE Y2", akts=5,
        C=[("Per", 18, 20, "H")],
        lab=[("g1 lab", [("Per", 20, 22, "T")]), ("g2 lab", [("Per", 20, 22, "Ç")])],
        kaynak="fiş (MSE booklet)",
    ),
    "CYB": dict(
        ad="Cybersecurity", prog="Lisans 4 (CTI/IOT)", akts=None,
        C=[("Pzt", 19, 21, "H")],
        lab=[("1241EC sgr2 lab", [("Cum", 19, 21, "T")]), ("1241EC sgr1 lab", [("Cum", 19, 21, "Ç")])],
        kaynak="ders adı + FILS müfredatı (fiş eldeki dosyalarda yok)",
    ),
    "IP": dict(
        ad="Image Processing", prog="Lisans 4", akts=None,
        C=[("Cum", 14, 16, "H")],
        lab=[("Erasmus lab", [("Sal", 8, 10, "H")])],
        kaynak="ders adı + FILS müfredatı",
    ),
    "ECG": dict(
        ad="Elements of Computer Graphics", prog="Lisans 3 (CTI)", akts=None,
        C=[("Çar", 18, 20, "H")],
        lab=[
            ("1231EA sgr1 lab", [("Sal", 16, 18, "H")]),
            ("1231EB sgr1 lab", [("Sal", 18, 20, "H")]),
            ("1231ED sgr1 lab", [("Çar", 12, 14, "H")]),
            ("1231EC sgr2 / EA sgr2 lab", [("Çar", 14, 16, "H")]),
            ("1231EC sgr1 / EB sgr2 lab", [("Çar", 16, 18, "H")]),
        ],
        kaynak="ders adı + FILS müfredatı",
    ),
    "ACG": dict(
        ad="Advanced Computer Graphics", prog="Lisans 3 (ETTI)", akts=None,
        C=[("Çar", 18, 20, "H")],
        lab=[("Erasmus lab", [("Cum", 20, 21, "H")])],
        kaynak="ders adı + FILS müfredatı",
    ),
    "FLC": dict(
        ad="Formal Languages and Compilers", prog="Lisans 3 (CTI)", akts=None,
        C=[("Sal", 14, 16, "H")],
        lab=[("Erasmus lab", [("Sal", 16, 18, "H")])],
        kaynak="ders adı + FILS müfredatı",
    ),
    "IOT": dict(
        ad="Internet of Things", prog="Lisans 3", akts=None,
        C=[("Per", 16, 18, "H")],
        lab=[("Erasmus lab (iki oturum)", [("Çar", 16, 18, "T"), ("Per", 14, 16, "Ç")])],
        kaynak="ders adı + FILS müfredatı",
    ),
    "GISS": dict(
        ad="Game and Interactive Simulation Systems", prog="MSE Y1", akts=4,
        C=[("Çar", 18, 20, "H")],
        lab=[("sg2 lab", [("Pzt", 14, 16, "H")]), ("sg3 lab (online)", [("Pzt", 18, 20, "H")])],
        kaynak="fiş (MSE booklet)",
    ),
    "PP": dict(
        ad="Programming Paradigms", prog="MSE Y1", akts=4,
        C=[("Pzt", 16, 18, "H")],  # 2-9. haftalar
        lab=[
            ("sg1 lab", [("Pzt", 8, 10, "H")]),
            ("sg3 lab (online)", [("Pzt", 14, 16, "H")]),
            ("sg2 lab", [("Cum", 18, 20, "H")]),
        ],
        kaynak="fiş (MSE booklet)",
    ),
    "FMSE": dict(
        ad="Formal Models in Software Engineering", prog="MSE Y1", akts=4,
        C=[("Sal", 16, 18, "H")],
        lab=[
            ("sg1 lab", [("Sal", 18, 20, "T")]),
            ("sg2 lab", [("Sal", 18, 20, "Ç")]),
            ("sg3 lab (online)", [("Per", 8, 10, "T")]),
        ],
        kaynak="fiş (MSE booklet)",
    ),
    "STSE": dict(
        ad="Special Topics in Software Engineering (IoT)", prog="MSE Y2", akts=3,
        C=[("Sal", 18, 20, "H")],
        lab=[("C+L birlikte", [])],
        kaynak="fiş (MSE booklet)",
    ),
    "SA": dict(
        ad="Software Architectures", prog="MSE Y2", akts=4,
        C=[("Per", 16, 18, "H")],
        lab=[("g1 lab (online)", [("Çar", 8, 10, "T")]), ("g2 lab (online)", [("Çar", 12, 14, "Ç")])],
        kaynak="fiş (MSE booklet)",
    ),
    "AI": dict(
        ad="Artificial Intelligence", prog="Lisans 4 (CTI)", akts=None,
        C=[("Sal", 8, 10, "H")],
        lab=[("Erasmus lab", [("Per", 8, 10, "H")])],
        kaynak="ders adı + FILS müfredatı",
    ),
    "NNGA": dict(
        ad="Project: Neural Networks and Genetic Algorithms", prog="Lisans 4 (ETTI)", akts=None,
        C=[],
        lab=[("1242EEA proje", [("Sal", 14, 16, "H")]), ("1242EB proje", [("Per", 14, 16, "H")])],
        kaynak="ders adı",
    ),
    "WEB": dict(
        ad="Web Applications - Project", prog="Lisans 4 (CTI)", akts=None,
        C=[],
        lab=[("1241EA proje", [("Pzt", 12, 14, "H")]), ("1241EB proje", [("Sal", 15, 17, "H")])],
        kaynak="ders adı",
    ),
    "OOP": dict(
        ad="Object Oriented Programming", prog="Lisans 2 (CTI)", akts=None,
        C=[("Cum", 12, 14, "H")],
        lab=[("Erasmus lab", [("Sal", 18, 21, "H")])],
        kaynak="ders adı + FILS müfredatı",
    ),
    "ISE": dict(
        ad="Intelligent Systems Engineering", prog="Lisans 4 (IOT)", akts=None,
        C=[("Çar", 16, 18, "H")],
        lab=[
            ("sgr1 lab + proje", [("Per", 16, 18, "T"), ("Cum", 8, 10, "Ç")]),
            ("sgr2 lab + proje", [("Per", 16, 18, "Ç"), ("Cum", 8, 10, "Ç")]),
        ],
        kaynak="ders adı",
    ),
}

# Teknik olarak programda olup SPM ile kesin çakışan dersler (bilgi için)
EN_CAKISAN = {
    "BIGDATA": ("Technologies for Big Data Analysis", "Per 18-20 ders saati = SPM ders saati"),
    "ST": ("Software Testing", "Çar 18-20 (eşleşen TR dersi yok)"),
}

# ---------------------------------------------------------------------------
# TR dersleri (24) ve içerik analizi.
# eslesme: [(EN kodu, güç 3=güçlü / 2=orta / 1=zayıf, örtüşen konular)]
# Programlara yalnızca güç >= 2 olan eşleşmeler alınır.
# ---------------------------------------------------------------------------
TR = [
    ("Güvenli Programlama",
     "OWASP, güvenli SDLC, girdi doğrulama, kimlik doğrulama/yetkilendirme, kriptografi, web güvenliği, güvenlik testleri",
     [("CYB", 2, "kriptografi, kimlik doğrulama, web saldırıları ve karşı önlemler; güvenli kodlama standardı kısmı yok"),
      ("SA", 1, "yalnızca mimari düzeyde güvenlik")]),
    ("İleri Python Programlama",
     "OOP (sınıf, kalıtım, polimorfizm), modüller, veri yapıları, NumPy/Pandas, scikit-learn, ağ programlama",
     [("PP", 2, "OOP + veri/kontrol soyutlama + çoklu paradigma; dil Java/Scala/Prolog (Python değil)"),
      ("OOP", 2, "sınıf/nesne, kalıtım, polimorfizm (haftalar 2-4); ML ve ağ kısmı yok"),
      ("AI", 1, "Python ile ML giriş haftaları ile kısmi")]),
    ("Kuantum Bilgi İşleme",
     "kübit, Hilbert uzayı, yoğunluk matrisi, kuantum devreleri, Grover/Shor, kuantum hata düzeltme, kuantum kriptografi",
     []),  # Quantum Physical Realizations (master) için ders programı yok
    ("Siber Güvenlik",
     "tehditler, kötü amaçlı yazılım, web saldırıları, ağ/OS güvenliği, bulut/DB güvenliği, KVKK, sosyal mühendislik, siber savaş",
     [("CYB", 3, "temel kavramlar, saldırılar, savunma, ağ/OS güvenliği — doğrudan karşılık")]),
    ("Gömülü Sistemler",
     "mikrodenetleyici, FSM, kesmeler, zamanlayıcı, PWM, ADC, LCD, UART/I2C/SPI",
     [("STSE", 3, "geliştirme kartları (Arduino/RPi), analog/dijital sensörler, aktüatörler, seri haberleşme SPI/I2C"),
      ("IOT", 2, "sensör/kart programlama, haberleşme protokolleri; FSM/PWM/ADC kısmı zayıf")]),
    ("Bulut Bilişim",
     "IaaS/PaaS/SaaS, dağıtım modelleri, sanallaştırma/konteyner, depolama/ağ, mikroservis, izleme, bulut güvenliği",
     [("SA", 2, "middleware, SOA, kurumsal entegrasyon, bileşen tabanlı mimari (mikroservis/SOA kısmı örtüşür)"),
      ("IOT", 1, "bulut servislerini kullanma (1 hafta)")]),
    ("Blokzincirin Temelleri",
     "DLT, hash, dijital imza, konsensüs, akıllı sözleşme, izinli/izinsiz ağlar",
     [("CYB", 1, "yalnızca kriptografi/hash kısmı")]),  # Blockchain protocols (master) için ders programı yok
    ("Adli Bilişim",
     "adli araçlar, dosya sistemi/veri kurtarma, görüntü iyileştirme ve manipülasyon analizi, ses, video, steganografi, zararlı yazılım",
     [("IP", 2, "görüntü iyileştirme, filtreleme, görüntü/video analizi (haftalar 4-5, 10-11)"),
      ("CYB", 1, "zararlı yazılım, adli bilişim ve siber suç haftası")]),
    ("Paralel Programlama",
     "paralel mimariler, SPMD/MIMD, thread/senkronizasyon, OpenMP, MPI, NUMA, paralel algoritmalar",
     []),  # Parallel programming (master) programda yok; Big Data (MapReduce) SPM ile çakışıyor
    ("Bulanık Mantık",
     "bulanık küme, üyelik fonksiyonları, T-norm, bulanık çıkarım (Mamdani, Sugeno), durulaştırma, Python",
     [("ISE", 1, "akıllı sistemler; bulanık mantık ayrı ünite olarak garanti değil"),
      ("AI", 1, "belirsizlik altında akıl yürütme")]),
    ("Makine Öğrenmesi",
     "denetimli/denetimsiz öğrenme, ön işleme, PCA/LDA, çapraz doğrulama, metrikler, ensemble, YOLO, derin öğrenme",
     [("AI", 2, "öğrenme algoritmaları, sınıflandırma; ön işleme/YOLO kısmı yok"),
      ("ISE", 2, "akıllı sistem tasarımı, öğrenen sistemler"),
      ("NNGA", 2, "sinir ağları ile öğrenme projesi")]),
    ("Optimizasyon Teknikleri",
     "kısıtsız/kısıtlı optimizasyon, doğrusal programlama, simpleks, sezgisel/metasezgisel yöntemler",
     [("NNGA", 1, "genetik algoritmalar = metasezgisel kısım")]),
    ("Bilgisayar Grafikleri",
     "2B/3B, dönüşüm matrisleri, rasterizasyon, renk modelleri, aydınlatma, Gouraud/Phong, ray tracing",
     [("ECG", 3, "dönüşümler, rasterizasyon, aydınlatma/gölgelendirme, render — doğrudan karşılık"),
      ("ACG", 3, "ileri render, aydınlatma, 3B grafik"),
      ("GISS", 1, "3B modeller")]),
    ("MATLAB Programlama",
     "MATLAB grafik/veri görselleştirme, 2B/3B çizim, istatistiksel grafikler",
     []),  # MATLAB odaklı İngilizce ders yok
    ("Ruby Programlama",
     "Ruby sözdizimi, OOP, modüller, Rails MVC, ActiveRecord, XSS/CSRF, REST API",
     [("WEB", 2, "MVC web uygulaması, veritabanı, REST, kimlik doğrulama (dil farklı)"),
      ("OOP", 2, "sınıf/nesne, kalıtım, kapsülleme, polimorfizm")]),
    ("Deneyim Mühendisliği",
     "UX, kullanıcı araştırması, prototipleme, UI tasarımı, kullanılabilirlik testi, mobil/web UX",
     [("GISS", 1, "HCI ünitesi")]),  # Applied HCI (master) için ders programı yok
    ("Fonksiyonel Programlama",
     "Haskell, liste, özyineleme, yüksek dereceli fonksiyon, tip denetimi, cebirsel tipler, tembel değerlendirme, monad",
     [("PP", 3, "Scala ile fonksiyonel programlama (6 saat ders + lab): özyineleme, jenerik tipler, liste, örüntü eşleme"),
      ("FMSE", 1, "operasyonel/denotasyonel semantik")]),
    ("Reaktif Programlama ve Sistemler",
     "veri akışları, olay tabanlı programlama, RxJava/Reactor, backpressure, reaktif mikroservis",
     [("SA", 1, "middleware/SOA/mesajlaşma"),
      ("AOSE", 1, "reaktif ajan mimarileri")]),
    ("Veri Madenciliği ve Bilgi Keşfi",
     "ön işleme, kümeleme, sınıflandırma, regresyon, Apriori, metin madenciliği, duygu analizi",
     []),  # Technologies for Big Data SPM ile çakışıyor
    ("Sosyal Ağ Analizi",
     "ağ modelleri, merkezilik, prestij, topluluk tespiti, küçük dünya ağları",
     []),
    ("Derleyici Tasarımı",
     "derleyici safhaları, bağlamdan bağımsız gramer, parsing, sembol tablosu, optimizasyon, kod üretimi",
     [("FLC", 3, "biçimsel diller, gramerler, otomatlar, ayrıştırma, derleyici safhaları — doğrudan karşılık"),
      ("FMSE", 2, "gramerler, otomatlar, DFA/NFA, düzenli ifadeler; kod üretimi yok")]),
    ("Yapay Sinir Ağları",
     "perceptron, Adaline, MLP, geri yayılım, CNN, RNN",
     [("NNGA", 3, "sinir ağları projesi — doğrudan karşılık"),
      ("AI", 2, "sinir ağları ünitesi"),
      ("ISE", 1, "öğrenen sistemler")]),
    ("Mühendislik Ekonomisi",
     "nakit akışı, faiz faktörleri, NPV, IRR, fayda/maliyet, amortisman, enflasyon, risk analizi",
     []),  # Money and Banking / Fundamentals of Management zayıf kalıyor
    ("Sanal ve Artırılmış Gerçeklik",
     "VR temelleri, 3B dönüşümler, quaternion, render, dokunsal arayüz, Unity3D, 3B UI",
     [("GISS", 3, "Unity 2B/3B, VR, HCI, Leap Motion — doğrudan karşılık"),
      ("ACG", 2, "render, 3B dönüşümler")]),
]

ZAYIF_EK = {
    # programlara girmeyen ama analizde belirtilen zayıf adaylar
    "Mühendislik Ekonomisi": "Money and Banking (faiz kısmı) / Fundamentals of Management — içerik örtüşmesi düşük",
    "MATLAB Programlama": "Control Theory ve Image Processing labları MATLAB kullanabilir — ders içeriği farklı",
    "Paralel Programlama": "Computer Architecture (paralel mimari kısmı) — zayıf; Technologies for Big Data (MapReduce) SPM ile çakışıyor",
    "Veri Madenciliği ve Bilgi Keşfi": "Technologies for Big Data Analysis (Hadoop, Hive, duygu analizi lab) — Per 18-20 SPM ile çakışıyor",
    "Optimizasyon Teknikleri": "Algorithm Design (Cum 14-16, Image Processing ile çakışır) — zayıf",
    "Kuantum Bilgi İşleme": "Quantum Physical Realizations (başka yüksek lisans) — elde ders programı yok",
    "Blokzincirin Temelleri": "Blockchain protocols and distributed applications (başka yüksek lisans) — elde ders programı yok",
    "Deneyim Mühendisliği": "Applied Human Computer Interaction (başka yüksek lisans) — elde ders programı yok",
    "Sosyal Ağ Analizi": "karşılık yok",
}

# Lisans dersleri için AKTS elde yok (ders programında yazmıyor, broşürlere erişilemedi).
# Tahmini varsayılanlar: ders + lab = 4, yalnızca proje = 3. Rapor sayfasında düzenlenebilir.
AKTS_TAHMIN = {"CYB": 4, "IP": 4, "ECG": 4, "ACG": 4, "FLC": 4, "IOT": 4, "AI": 4, "OOP": 4, "ISE": 4,
               "WEB": 3, "NNGA": 3}
for _k, _v in AKTS_TAHMIN.items():
    EN[_k]["akts"] = _v
    EN[_k]["akts_tahmini"] = True
