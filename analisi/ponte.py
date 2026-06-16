#!/usr/bin/env python3
"""Ponte verso il vector database (repo gemello).

Le analisi qui si appoggiano sull'indice LanceDB costruito dal repo
`vectordatabase-documenti-papi`: questo modulo lo rende raggiungibile e importa
`vdb` (Embedder + primitive + ricerca ibrida). La posizione del repo si configura
con la variabile d'ambiente VDB_REPO; di default è il repo gemello, accanto a
questo.

    from ponte import vdb, tabella
    tab = tabella()        # la tabella 'chunk' dell'indice
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
        f"vector database non trovato in {VDB_REPO}. "
        "Imposta la variabile d'ambiente VDB_REPO al percorso del repo "
        "vectordatabase-documenti-papi.")

sys.path.insert(0, str(VDB_REPO))
import vdb  # noqa: E402

INDICE = VDB_REPO / "indice"


def tabella():
    """Apre la tabella 'chunk' dell'indice LanceDB del vector database."""
    if not INDICE.exists():
        raise RuntimeError(
            f"indice LanceDB assente in {INDICE}. Costruiscilo con "
            "`python vdb.py build` nel repo del vector database.")
    return vdb.lancedb.connect(str(INDICE)).open_table("chunk")
