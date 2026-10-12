"""Çakışmasız tüm programları üretir.

Kurallar:
  * SPM (Software Project Management) her programda var (Bitirme karşılığı).
  * Her TR dersi en fazla bir İngilizce derse, her İngilizce ders en fazla bir TR dersine eşlenir.
  * Yalnızca içerik gücü >= 2 (orta/güçlü) eşleşmeler kullanılır.
  * Ders + seçilen lab/proje saatleri hiçbir haftada çakışmaz (tek/çift hafta dikkate alınır).
  * Erasmus labı olan derslerde yalnızca Erasmus labı seçilir.
  * Sadece "maksimal" programlar listelenir: eklenebilecek başka uyumlu TR dersi kalmamış olmalı.
"""
import itertools
import json

from data import EN, TR

MIN_GUC = 2


def weeks(w):
    return {"H": {0, 1}, "T": {1}, "Ç": {0}}[w]


def clash(a, b):
    d1, s1, e1, w1 = a
    d2, s2, e2, w2 = b
    return d1 == d2 and s1 < e2 and s2 < e1 and weeks(w1) & weeks(w2)


def slots_ok(slots):
    return not any(clash(a, b) for a, b in itertools.combinations(slots, 2))


def options(code):
    """Bir İngilizce dersin olası (lab adı, tüm saatler) seçenekleri."""
    c = EN[code]
    return [(name, list(c["C"]) + list(s)) for name, s in c["lab"]]


def feasible_configs(codes):
    """Dersler listesi için çakışmasız tüm lab kombinasyonları."""
    out = []
    for combo in itertools.product(*(options(c) for c in codes)):
        slots = [s for _, ss in combo for s in ss]
        if slots_ok(slots):
            out.append({c: name for c, (name, _) in zip(codes, combo)})
    return out


def main():
    cands = []
    for i, (ad, _, es) in enumerate(TR):
        good = [(c, g) for c, g, _ in es if g >= MIN_GUC and c in EN]
        if good:
            cands.append((i, good))

    results = {}

    def rec(k, assign, used):
        if k == len(cands):
            codes = ["SPM"] + [c for _, c in assign]
            cfgs = feasible_configs(codes)
            if cfgs:
                key = tuple(sorted(assign))
                results[key] = cfgs
            return
        i, good = cands[k]
        # dersi alma
        rec(k + 1, assign, used)
        for c, _ in good:
            if c in used:
                continue
            new = assign + [(i, c)]
            if feasible_configs(["SPM"] + [x for _, x in new]):
                rec(k + 1, new, used | {c})

    rec(0, [], frozenset())

    # maksimal olanları bırak
    keys = list(results)
    sets = {k: set(k) for k in keys}
    trsets = {k: {i for i, _ in k} for k in keys}

    def extendable(k):
        # aynı eşlemeler + en az bir ek TR dersi içeren başka geçerli program var mı
        return any(sets[k] < sets[o] for o in keys)

    maximal = [k for k in keys if not extendable(k)]

    guc = {(i, c): g for i, (_, _, es) in enumerate(TR) for c, g, _ in es}

    def score(k):
        return (len(k), sum(guc[p] for p in k))

    maximal.sort(key=lambda k: score(k), reverse=True)
    out = []
    for n, k in enumerate(maximal, 1):
        out.append(dict(
            no=n,
            eslesme=[dict(tr=TR[i][0], en=c, guc=guc[(i, c)]) for i, c in sorted(k)],
            ders_sayisi=len(k),
            guc_toplam=sum(guc[p] for p in k),
            lab_secenekleri=results[k],
        ))
    print(f"aday TR dersi: {len(cands)}, geçerli program: {len(results)}, maksimal: {len(maximal)}")
    from collections import Counter
    print(Counter(len(k) for k in maximal))
    json.dump(out, open("programs.json", "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
