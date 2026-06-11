# textmining-documenti-papi

Le **analisi** sul corpus dei documenti dei Papi: rispondere, sui dati, alle
domande da cui è partito tutto il progetto. È l'ultimo stadio — quello che
trasforma i testi indicizzati in **risposte e racconto**.

## Da dove nasce

Una domanda grande tra amici che leggono i giornali. Di che cosa parlano
*davvero* i Papi? C'è continuità tra un pontificato e l'altro? Quando un titolo
riassume un Papa in una parola — i migranti, l'ambiente — è il Papa o è il
giornale? Discorsi che scivolano in fretta sul senso della vita e sulla fede, e
la voglia di **verificarli sui dati** invece di tirare a indovinare.

I due repository a monte preparano il terreno; qui si fanno le domande.

## Posto nel progetto

```
ingestion-documenti-papi   →  scarica i documenti raw (markdown)
vectordatabase-...         →  spezza, fa gli embeddings, indicizza, cerca
textmining-... (questo)    →  analisi e racconto sui dati
```

Le analisi qui si appoggiano sui **dati arricchiti** del vector database (topic,
entità, sentiment, frame valoriali): lì si aggiungono i campi, qui si
interrogano e si raccontano.

## Le domande a cui rispondere

Le domande nate nel 2019, e come potremmo affrontarle con le tecniche di oggi.
Sono il punto di partenza, **non una lista chiusa**: durante il lavoro
evolveranno e se ne aggiungeranno altre.

| Domanda | Come rispondere oggi |
|---|---|
| Di cosa parla l'ultimo Papa? Solo migranti? | Topic modeling + keyness + conteggio concetti nel tempo; RAG per le citazioni |
| C'è continuità tra gli ultimi tre Papi? | Confronto topic/lessico per pontificato; distanza semantica fra corpora |
| *(nuova)* Evoluzione di pace, ambiente, misericordia? | Dynamic topic modeling con change-point sulle date |
| *(nuova)* Quali frame morali/valoriali ricorrono? | Annotazione di frame morali/valoriali (language-based preferences / LENS) |

> Le tecniche sono indicazioni di metodo, non scelte definitive: si decideranno
> sui dati, strada facendo.

## Forma delle analisi (da definire)

Non è ancora deciso *come* verranno fatte ed esposte le analisi. Le ipotesi
sul tavolo:

- analisi **one-shot** (script o notebook che producono un risultato);
- **dashboard** interattive;
- **data visualization** e grafici;
- **notebook** o documenti **markdown** narrativi.

Il racconto — quale storia raccontano i dati, e in che forma — è parte del
lavoro da fare, non un dato di partenza.

## Stato

Scaffold iniziale: solo le domande e la direzione. Il codice delle analisi
arriverà man mano che i dati arricchiti del vector database saranno disponibili.
