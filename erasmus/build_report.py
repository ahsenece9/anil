"""programs.json + data.py -> rapor.html (tek dosya, interaktif)."""
import json
from collections import defaultdict

from data import EN, EN_CAKISAN, TR, ZAYIF_EK

progs = json.load(open("programs.json"))

# İngilizce ders setine göre grupla (aynı derslere giriliyor, sadece TR eşleştirmesi farklı)
groups = defaultdict(list)
for p in progs:
    key = tuple(sorted(e["en"] for e in p["eslesme"]))
    groups[key].append(p)

paket = []
for key, ps in groups.items():
    ps.sort(key=lambda p: -p["guc_toplam"])
    paket.append(dict(
        en=list(key),
        varyant=[[{"tr": e["tr"], "en": e["en"], "guc": e["guc"]} for e in p["eslesme"]] for p in ps],
        guc=ps[0]["guc_toplam"],
        lab=ps[0]["lab_secenekleri"],
    ))
paket.sort(key=lambda g: (-len(g["en"]), -g["guc"], g["en"]))
for i, g in enumerate(paket, 1):
    g["no"] = i

en_out = {k: dict(ad=v["ad"], prog=v["prog"], akts=v["akts"], C=v["C"],
                  lab=[[n, s] for n, s in v["lab"]], kaynak=v["kaynak"]) for k, v in EN.items()}
en_out["SPM"]["not"] = "Bitirme karşılığı — her programda sabit"
tr_out = [dict(ad=a, konu=k, es=[dict(en=c, guc=g, not_=n) for c, g, n in es], zayif=ZAYIF_EK.get(a, ""))
          for a, k, es in TR]

DATA = dict(en=en_out, tr=tr_out, paket=paket,
            cakisan=[dict(kod=k, ad=a, neden=n) for k, (a, n) in EN_CAKISAN.items()],
            toplam_varyant=len(progs))

tpl = open("template.html", encoding="utf-8").read()
html = tpl.replace("/*__DATA__*/null", json.dumps(DATA, ensure_ascii=False))
open("rapor.html", "w", encoding="utf-8").write(html)
print("paket:", len(paket), "varyant:", len(progs))
