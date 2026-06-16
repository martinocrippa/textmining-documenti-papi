# articles/ — gli articoli divulgativi

Le analisi raccontate come **articoli da rivista**, per chi è curioso ma non
mastica statistica. Niente gergo tecnico: i numeri restano (le percentuali si
capiscono), ma la storia viene prima. I dati e i metodi per esteso stanno nei
notebook in [`../analisi/`](../analisi/).

| Articolo | Di cosa parla |
|---|---|
| [Di cosa parlano davvero i Papi](01-di-cosa-parlano-i-papi.md) | La domanda grande: continuità, accenti, e quel "comunista" da bar. |
| [Hanno mantenuto le promesse?](02-hanno-mantenuto-le-promesse.md) | Il programma del primo giorno regge per tutto il pontificato? |
| [Parole o significato](03-parole-o-significato.md) | Come si fa a misurare "di cosa parla" un Papa — senza barare. |
| [Appendice tecnica](appendice-tecnica.md) | Il *come* di ogni numero: affermazione per affermazione, col metodo in chiaro. Ponte verso i notebook. |

Negli articoli, le note a piè di pagina rimandano alla sezione giusta
dell'appendice (e quindi al notebook con il codice).

## Esportare in PDF

I file sono markdown con le immagini in [`immagini/`](immagini/) (percorsi
relativi, così l'export resta autoconsistente). Con [pandoc](https://pandoc.org):

```bash
pandoc 01-di-cosa-parlano-i-papi.md -o 01-di-cosa-parlano-i-papi.pdf
```

## Le figure

In [`immagini/`](immagini/). Le figure di sintesi (continuità, "comunista",
struttura, mandato) si **rigenerano** da [`genera_figure.py`](genera_figure.py)
(`python genera_figure.py`), che parte dai numeri aggregati delle analisi. Le altre
due (`temi_per_papa`, `argomenti-nel-tempo`) le producono i notebook 01 e 07.

## La regola di sempre

Solo viste **aggregate** (percentuali, andamenti): nessun testo dei Papi è
riprodotto qui. I documenti restano © Libreria Editrice Vaticana, uso personale e
di studio.
