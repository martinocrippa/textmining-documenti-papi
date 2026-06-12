# Setup dell'ambiente

Il text mining richiede **Python ≥ 3.9** (consigliato 3.12). La baseline è per
**viste aggregate, notebook e data visualization**: `pandas`, `numpy`,
`pyarrow`, `matplotlib`, `jupyter`. Le librerie specifiche delle analisi (topic
modeling, NLP, dashboard) si aggiungono man mano che le analisi vengono scelte.

> Parte di un progetto in tre repository indipendenti (ingestion → vector
> database → text mining): ognuno ha il proprio `setup/`, da installare a sé.

## Opzione A — conda (consigliata)

```bash
conda env create -f setup/environment.yml
conda activate textmining-papi
```

Per aggiornarlo dopo una modifica al file:

```bash
conda env update -f setup/environment.yml --prune
```

## Opzione B — venv + pip

```bash
python -m venv .venv
# Windows:        .venv\Scripts\activate
# Linux/macOS:    source .venv/bin/activate
pip install -r requirements.txt
```

## Verifica

Con l'ambiente **attivo** (`python` = Python 3 dell'ambiente):

```bash
python -c "import pandas, numpy, pyarrow, matplotlib; print('ok')"
jupyter --version
```

> I dati arricchiti su cui lavorano le analisi arrivano dal repo del vector
> database e restano locali (non versionati): vedi il README principale e la
> regola "viste aggregate" sul copyright.
