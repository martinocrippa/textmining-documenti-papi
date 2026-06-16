# analisi/ — le analisi sui dati

Piccole analisi **rieseguibili**, una per domanda, come notebook. Si appoggiano
sull'indice LanceDB del *vector database* (repo gemello) tramite il ponte
[`ponte.py`](ponte.py): nessun testo è copiato qui, solo viste **aggregate**.

## I notebook

| Notebook | Domanda | In una riga |
|---|---|---|
| [`01-temi-per-papa.ipynb`](01-temi-per-papa.ipynb) | Di cosa parlano i Papi? C'è continuità? Francesco è comunista? | Temi per Papa, parole vs significato, con heatmap. Continuità piena, accenti diversi, comunismo no. |
| [`02-parole-vs-significato.ipynb`](02-parole-vs-significato.ipynb) | Come si misura un tema: parole o significato? E con che metodo? | Perché la ricerca è **ibrida** e perché si confrontano distribuzioni e non soglie. Più il footprint calcio/ambiente. |

## Come si eseguono

1. **L'indice deve esistere.** Costruiscilo nel repo del vector database:
   `python vdb.py build` (genera `indice/`, locale). Di default i notebook
   cercano il repo gemello accanto a questo; per un percorso diverso imposta la
   variabile d'ambiente `VDB_REPO`.
2. **Ambiente** con le librerie delle analisi (`sentence-transformers`,
   `lancedb`, `torch`, `seaborn`, `jupyter`): vedi [`../setup/`](../setup/).
3. Apri i notebook (`jupyter lab` o l'estensione dell'editor) e *Run All*. Il
   calcolo embedding gira sulla CPU: un paio di minuti il primo notebook.

> Su Windows il prodotto matrice-vettore va fatto in **torch** (non numpy): dopo
> aver caricato torch, il BLAS di numpy può far crashare il processo (conflitto
> MKL). I notebook lo fanno già così.

## La regola del repo

Si versiona solo **codice rieseguibile** e **figure aggregate** (le heatmap
`.png`). I testi restano © Libreria Editrice Vaticana, locali e in `.gitignore`;
nelle analisi compaiono solo conteggi, percentuali e trend — mai i documenti.
