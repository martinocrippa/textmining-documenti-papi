#!/usr/bin/env python3
"""Ponte verso il vector database (repo gemello).

Le analisi qui si appoggiano sull'indice LanceDB costruito dal repo
`vectordatabase-documenti-papi`. La posizione del repo si configura con la
variabile d'ambiente VDB_REPO; di default è il repo gemello, accanto a questo.

    from ponte import tabella, embedder
    tab = tabella()        # la tabella 'chunk' (solo lancedb, NIENTE torch)
    emb = embedder()       # il modello e5 (importa vdb → torch), solo se serve

`tabella()` non importa vdb/torch: le analisi che leggono i vettori già
indicizzati (es. il topic modeling) restano leggere e non caricano il modello.
"""

from __future__ import annotations

import os
import pathlib
import sys

QUI = pathlib.Path(__file__).resolve()
VDB_REPO = pathlib.Path(
    os.environ.get("VDB_REPO", QUI.parents[2] / "vectordatabase-documenti-papi"))

if not (VDB_REPO / "vdb.py").exists():
    raise RuntimeError(
        f"vector database non trovato in {VDB_REPO}. Imposta la variabile "
        "d'ambiente VDB_REPO al percorso del repo vectordatabase-documenti-papi.")

sys.path.insert(0, str(VDB_REPO))
INDICE = VDB_REPO / "indice"


def tabella():
    """Apre la tabella 'chunk' dell'indice LanceDB (solo lancedb, niente torch)."""
    import lancedb
    if not INDICE.exists():
        raise RuntimeError(
            f"indice LanceDB assente in {INDICE}. Costruiscilo con "
            "`python vdb.py build` nel repo del vector database.")
    return lancedb.connect(str(INDICE)).open_table("chunk")


def embedder():
    """Il modello e5 per vettorializzare nuove query (importa vdb → torch)."""
    import vdb
    return vdb.Embedder()
