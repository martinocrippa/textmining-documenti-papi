#!/usr/bin/env python3
"""esplora_temi.py — piccola esplorazione visuale: di cosa parlano i Papi.

NON e' il "profilo per argomenti" (quello e' l'idea grande nel README: temi al
netto del dovuto da ruolo/liturgia, mandati dichiarati). Qui solo una heatmap
esplorativa sui conteggi gia' a disposizione.

Heatmap temi x Papi: il COLORE e' il `lift` (scala divergente centrata su 1 —
bianco = come tutti, rosso = ne parla piu' della media, blu = meno); il NUMERO in
cella e' la `% di documenti` (il "quanto" grezzo). Due blocchi: i temi piu'
distintivi sopra, quelli che tornano per tutti sotto — che restano quasi tutti
bianchi (lift ~ 1).

Dati: % e lift per Papa (dal check di ingestion). Esplorativo, non di produzione.
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm

PAPI = ["GP2", "BXVI", "FRA", "LEO"]

# tema -> (% , lift) per i 4 Papi, nell'ordine di PAPI
DISTINTIVI = {
    "poveri":          [(33, .85), (35, .90), (46, 1.18), (42, 1.08)],
    "migranti":        [(6, .73),  (6, .73),  (12, 1.45), (9, 1.09)],
    "giustizia":       [(5, .74),  (5, .74),  (10, 1.48), (7, 1.04)],
    "ric./ricchezza":  [(5, .80),  (5, .80),  (8, 1.28),  (7, 1.12)],
    "lavoro":          [(12, 1.60), (6, .80), (7, .93),   (5, .67)],
    "ambiente":        [(18, 1.03), (15, .86), (19, 1.09), (18, 1.03)],
}
DOMINANTI = {
    "pace":            [(54, .86), (58, .92), (59, .94), (80, 1.27)],
    "famiglia":        [(54, 1.03), (55, 1.05), (51, .97), (50, .95)],
    "Dio/Vangelo":     [(88, 1.02), (88, 1.02), (82, .95), (86, 1.00)],
}

# ordine: distintivi (in alto) -> separatore -> dominanti (in basso)
temi = list(DISTINTIVI) + ["— tornano per tutti —"] + list(DOMINANTI)
righe_dati = {**DISTINTIVI, **DOMINANTI}

# matrici lift (colore) e % (annotazione); la riga separatore e' NaN/vuota
lift = np.full((len(temi), len(PAPI)), np.nan)
pct = [["" for _ in PAPI] for _ in temi]
for i, t in enumerate(temi):
    if t not in righe_dati:
        continue
    for j, (p, l) in enumerate(righe_dati[t]):
        lift[i, j] = l
        pct[i][j] = f"{p}%\n×{l:.2f}"

fig, ax = plt.subplots(figsize=(6.2, 6.4))
norm = TwoSlopeNorm(vmin=0.6, vcenter=1.0, vmax=1.6)
cmap = plt.cm.RdBu_r.copy()
cmap.set_bad("#f2f2f2")                       # riga separatore in grigio
im = ax.imshow(lift, cmap=cmap, norm=norm, aspect="auto")

ax.set_xticks(range(len(PAPI)), PAPI, fontsize=11)
ax.set_yticks(range(len(temi)), temi, fontsize=10)
ax.xaxis.set_label_position("top")
ax.xaxis.tick_top()

for i in range(len(temi)):
    for j in range(len(PAPI)):
        if not pct[i][j]:
            continue
        # testo scuro su celle pallide, chiaro sulle estreme
        v = lift[i, j]
        scuro = 0.85 <= v <= 1.18
        ax.text(j, i, pct[i][j], ha="center", va="center",
                fontsize=8.5, color="black" if scuro else "white")

ax.set_title("Di cosa parlano i Papi — esplorazione\ncolore = lift (rosso: piu' della media) · numero = % documenti",
             fontsize=11, pad=12)
cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04, extend="both")
cbar.set_label("lift (1 = come tutti)", fontsize=9)
cbar.ax.axhline(norm(1.0), color="black", lw=0.8)
fig.tight_layout()

out = "esplora_temi.png"
fig.savefig(out, dpi=150, bbox_inches="tight")
print(f"salvato {out}")