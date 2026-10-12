"""data.py + programs.json -> rapor.html (tek dosya, interaktif).

Sayfa, SPM ile birlikte çakışmasız olan ve geçerli TR eşleştirmesi bulunan TÜM İngilizce ders kümelerini taşır.
AKTS alt/üst sınırı ve "sınır içinde maksimal" filtresi tarayıcıda hesaplanır (AKTS değerleri sayfada düzenlenebilir).
"""
import itertools
import json

from data import EN, EN_CAKISAN, TR, ZAYIF_EK
from solver import MIN_GUC, feasible_configs

MAX_LAB = 4  # sayfada gösterilecek lab kombinasyonu sayısı (fazlası sayılır)

progs = json.load(open("programs.json"))

# Maksimal programların tüm alt kümeleri de geçerlidir (ders çıkarmak çakışma yaratmaz).
sets = set()
for p in progs:
    ens = sorted(e["en"] for e in p["eslesme"])
    for r in range(1, len(ens) + 1):
        sets.update(itertools.combinations(ens, r))

# EN -> TR adayları (güç >= MIN_GUC)
cand = {}
for i, (_, _, es) in enumerate(TR):
    for c, g, _ in es:
        if g >= MIN_GUC and c in EN:
            cand.setdefault(c, []).append((i, g))


def assignments(ens):
    """Her İngilizce derse farklı bir TR dersi atayan tüm eşleştirmeler."""
    out = []

    def rec(k, used, acc):
        if k == len(ens):
            out.append(list(acc))
            return
        for i, g in cand[ens[k]]:
            if i not in used:
                rec(k + 1, used | {i}, acc + [(i, ens[k], g)])

    rec(0, frozenset(), [])
    return out


kumeler = []
for s in sorted(sets, key=lambda s: (-len(s), s)):
    s = list(s)
    asg = assignments(s)
    best = max(sum(g for *_, g in a) for a in asg)
    asg.sort(key=lambda a: -sum(g for *_, g in a))
    labs = feasible_configs(["SPM"] + s)
    kumeler.append(dict(
        en=s, guc=best,
        varyant=[[[i, c, g] for i, c, g in a] for a in asg[:3]], nvar=len(asg),
        lab=labs[:MAX_LAB], nlab=len(labs),
    ))

en_out = {k: dict(ad=v["ad"], prog=v["prog"], akts=v["akts"], tahmini=v.get("akts_tahmini", False), C=v["C"],
                  lab=[[n, s] for n, s in v["lab"]], kaynak=v["kaynak"]) for k, v in EN.items()}
tr_out = [dict(ad=a, konu=k, es=[dict(en=c, guc=g, not_=n) for c, g, n in es], zayif=ZAYIF_EK.get(a, ""))
          for a, k, es in TR]

DATA = dict(en=en_out, tr=tr_out, kume=kumeler,
            cakisan=[dict(kod=k, ad=a, neden=n) for k, (a, n) in EN_CAKISAN.items()])

tpl = open("template.html", encoding="utf-8").read()
open("rapor.html", "w", encoding="utf-8").write(tpl.replace("/*__DATA__*/null", json.dumps(DATA, ensure_ascii=False, separators=(",", ":"))))
print("küme:", len(kumeler))
