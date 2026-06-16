# analisi/ — le analisi sui dati

Piccole analisi **rieseguibili**, una per domanda, come notebook. Si appoggiano
sull'indice LanceDB del *vector database* (repo gemello) tramite il ponte
[`ponte.py`](ponte.py): nessun testo è copiato qui, solo viste **aggregate**.

## I notebook

| Notebook | Domanda | In una riga |
|---|---|---|
| [`01-temi-per-papa.ipynb`](01-temi-per-papa.ipynb) | Di cosa parlano i Papi? C'è continuità? Francesco è comunista? | Temi per Papa, parole vs significato, con heatmap. Continuità piena, accenti diversi, comunismo no. |
| [`02-parole-vs-significato.ipynb`](02-parole-vs-significato.ipynb) | Come si misura un tema: parole o significato? E con che metodo? | Perché la ricerca è **ibrida** e perché si confrontano distribuzioni e non soglie. Più il footprint calcio/ambiente. |
| [`03-topic-emergenti.ipynb`](03-topic-emergenti.ipynb) | E se i temi li lasciamo **emergere** dai dati invece di sceglierli? | KMeans sugli embedding + c-TF-IDF: emergono la linea rossa liturgica, lo strato "dovuto" dal ruolo e le firme dei singoli Papi. Primo passo della topic extraction. |
| [`04-struttura-argomenti.ipynb`](04-struttura-argomenti.ipynb) | La nostra ipotesi di argomenti, strutturata e **marcata** sui dati | Sei famiglie con un'ancora semantica; ogni **chunk** prende la sua (i discorsi si mischiano). La linea rossa è ~80% per tutti; le differenze stanno nella fascia sottile (attualità FRA/LEO, viaggi GP2). |
| [`05-mandato.ipynb`](05-mandato.ipynb) | Hanno tenuto il **mandato** dichiarato all'inizio? | Vettore-mandato = baricentro dell'omelia di inizio pontificato; fedeltà anno per anno. Trend piatto per tutti = nessuna deriva (GP2 stabile su 27 anni). |
| [`07-argomenti-nel-tempo.ipynb`](07-argomenti-nel-tempo.ipynb) | Gli argomenti **estratti** dal dato, seguiti nel tempo (dentro e tra i Papi) | Topic extraction vera (modello condiviso) + heatmap argomento × anno: continuità del fondo e ondate legate ai Papi (Santa Marta di Francesco, il sociale che sale, l'America Latina di GP2 che cala). |

> La **sintesi divulgativa** delle conclusioni (per un pubblico non tecnico) è in
> [`../docs/`](../docs/), con appendice tecnica. (Il vecchio notebook
> `06-sintesi` è confluito lì.)

## Come si eseguono

1. **L'indice deve esistere.** Costruiscilo nel repo del vector database:
   `python vdb.py build` (genera `indice/`, locale). Di default i notebook
   cercano il repo gemello accanto a questo; per un percorso diverso imposta la
   variabile d'ambiente `VDB_REPO`.
2. **Ambiente** con le librerie delle analisi (`sentence-transformers`,
   `lancedb`, `torch`, `seaborn`, `scikit-learn`, `jupyter`): vedi
   [`../setup/`](../setup/).
3. Apri i notebook (`jupyter lab` o l'estensione dell'editor) e *Run All*. Il
   calcolo embedding gira sulla CPU: un paio di minuti il primo notebook.

> **Nota Windows / OpenMP.** Su alcuni env conda con MKL + torch c'è un doppio
> `libiomp5md.dll` che fa crashare il codice nativo pesante: i notebook 01/04/05
> fanno il prodotto matrice-vettore in **torch** (non numpy) apposta; il 03 e il 07
> usano `KMeans` di scikit-learn, che usa OpenMP e può cadere lo stesso. Se càpita,
> gira in un ambiente "sano" (numpy non-MKL, es. `conda install nomkl`, o un env
> pip-only).

## La regola del repo

Si versiona solo **codice rieseguibile** e **figure aggregate** (le heatmap
`.png`). I testi restano © Libreria Editrice Vaticana, locali e in `.gitignore`;
nelle analisi compaiono solo conteggi, percentuali e trend — mai i documenti.
