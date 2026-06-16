#!/usr/bin/env python3
"""Rigenera le figure di sintesi degli articoli in immagini/.

I numeri qui sotto sono i **risultati aggregati** delle analisi (notebook 01/04/05);
sono riportati anche nell'appendice tecnica. Questo script li trasforma in figure
ed è l'unico posto da cui le figure-articolo si rigenerano. Le altre due immagini
(`temi_per_papa.png`, `argomenti-nel-tempo.png`) le producono i notebook 01 e 07.

Gira in un Python con matplotlib (es. il base di conda). Uso:
    python genera_figure.py
"""

import pathlib

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

IMG = pathlib.Path(__file__).resolve().parent / "immagini"
IMG.mkdir(exist_ok=True)
AB = ["GP2", "BXVI", "FRA", "LEO"]
COLP = {"GP2": "#4C72B0", "BXVI": "#55A868", "FRA": "#C44E52", "LEO": "#8172B3"}
x = np.arange(4)


def _grouped(ax, dati, w, titolo, ylab="% di documenti", ylim=100):
    for i, (t, v) in enumerate(dati.items()):
        ax.bar(x + (i - (len(dati) - 1) / 2) * w, v, w, label=t)
    ax.set_xticks(x); ax.set_xticklabels(AB); ax.set_ylabel(ylab)
    if ylim:
        ax.set_ylim(0, ylim)
    ax.set_title(titolo)
    ax.legend(fontsize=8, ncol=len(dati), loc="upper center", bbox_to_anchor=(0.5, -0.1))


# --- continuità a significato: temi dominanti (embedding) + nucleo condiviso ---
def continuita_significato():
    dom = {"Dio / Vangelo": [88, 86, 85, 87], "pace": [52, 46, 47, 58], "famiglia": [52, 51, 60, 55]}
    core = [79.1, 80.9, 82.1, 79.4]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.3))
    _grouped(a1, dom, 0.26, "Temi dominanti, misurati a SIGNIFICATO\n(non a parole): identici per tutti")
    a2.bar(x, core, 0.55, color="#dd8452")
    for i, v in enumerate(core):
        a2.text(i, v + 1.5, f"{v:.0f}%", ha="center", fontsize=10)
    a2.axhline(np.mean(core), ls="--", color="gray", lw=1)
    a2.set_xticks(x); a2.set_xticklabels(AB); a2.set_ylim(0, 100); a2.set_ylabel("% dei passaggi")
    a2.set_title("Il nucleo condiviso (fede, devozione, liturgia)\nmarcato per significato: ~80% per ognuno")
    fig.suptitle("La continuità vista dagli embedding — non solo a parole", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95]); fig.savefig(IMG / "sintesi-continuita-significato.png", dpi=150, bbox_inches="tight"); plt.close(fig)


# --- "comunista?": temi sociali (regex) ---
def comunista():
    soc = {"poveri": [33, 36, 46, 41], "migranti": [6, 6, 12, 9], "giustizia": [6, 6, 10, 8], "lavoro (operai)": [12, 7, 8, 6]}
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    _grouped(ax, soc, 0.2, "«Comunista?» Francesco accentua i poveri,\nma sul lavoro il primo è Giovanni Paolo II")
    fig.tight_layout(); fig.savefig(IMG / "sintesi-comunista.png", dpi=150, bbox_inches="tight"); plt.close(fig)


# --- struttura per famiglie: composizione + zoom fascia sottile ---
def struttura():
    FAM = ["liturgia", "fede e devozione", "eventi e ricorrenze", "viaggi", "programma e storia", "attualità"]
    M = np.array([[3.4, 3.7, 1.7, 2.3], [75.7, 77.2, 80.4, 77.1], [3.4, 2.1, 1.7, 2.4],
                  [9.9, 8.3, 5.4, 7.6], [5.3, 6.7, 5.3, 6.4], [2.3, 1.9, 5.5, 4.3]])
    cmap = plt.cm.tab20.colors
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.4))
    left = np.zeros(4)
    for k, fn in enumerate(FAM):
        a1.barh(x, M[k], left=left, color=cmap[k * 2 % 20], label=fn); left += M[k]
    a1.set_yticks(x); a1.set_yticklabels(AB); a1.invert_yaxis(); a1.set_xlim(0, 100)
    a1.set_xlabel("% dei chunk"); a1.set_title("Di cosa parlano: la linea rossa è ~80% per tutti")
    a1.legend(fontsize=8, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.15))
    sub = [0, 2, 3, 4, 5]; w = 0.16
    for j, k in enumerate(sub):
        a2.bar(x + (j - 2) * w, M[k], w, color=cmap[k * 2 % 20], label=FAM[k])
    a2.set_xticks(x); a2.set_xticklabels(AB); a2.set_ylabel("% dei chunk")
    a2.set_title("La fascia sottile: attualità (FRA/LEO) e viaggi (GP2)")
    a2.legend(fontsize=8, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.15))
    fig.tight_layout(); fig.savefig(IMG / "sintesi-struttura.png", dpi=150, bbox_inches="tight"); plt.close(fig)


# --- tenuta del mandato nel tempo (serie = output del notebook 05) ---
def mandato():
    serie = {
        "GP2": [[1978, .9123], [1979, .9113], [1980, .9115], [1981, .9102], [1982, .9094], [1983, .9112], [1984, .9103], [1985, .9103], [1986, .9102], [1987, .9107], [1988, .9102], [1989, .9096], [1990, .91], [1991, .9096], [1992, .9096], [1993, .9092], [1994, .9079], [1995, .9075], [1996, .9042], [1997, .904], [1998, .9012], [1999, .9036], [2000, .9039], [2001, .9025], [2002, .9004], [2003, .9027], [2004, .9017], [2005, .9016]],
        "BXVI": [[2005, .9066], [2006, .9068], [2007, .9061], [2008, .9064], [2009, .906], [2010, .9065], [2011, .9081], [2012, .9103], [2013, .9117]],
        "FRA": [[2013, .8965], [2014, .8955], [2015, .8965], [2016, .8959], [2017, .8945], [2018, .8953], [2019, .8941], [2020, .897], [2021, .8965], [2022, .8964], [2023, .8944], [2024, .8937], [2025, .895]],
        "LEO": [[2025, .907], [2026, .9063]],
    }
    fig, ax = plt.subplots(figsize=(8, 4.4))
    for a in AB:
        s = serie[a]
        ax.plot([p[0] for p in s], [p[1] for p in s], "o-", ms=3, color=COLP[a], label=a)
    ax.set_ylim(0.85, 0.93); ax.set_xlabel("anno"); ax.set_ylabel("similarità media al mandato")
    ax.set_title("Tenuta del mandato: nessuna deriva (GP2 piatto su 27 anni)")
    ax.legend(fontsize=9); ax.grid(alpha=.3)
    fig.tight_layout(); fig.savefig(IMG / "sintesi-mandato.png", dpi=150, bbox_inches="tight"); plt.close(fig)


if __name__ == "__main__":
    continuita_significato(); comunista(); struttura(); mandato()
    print("figure di sintesi rigenerate in", IMG)
