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
vectordatabase-...         →  spezza, fa gli embeddings, indicizza, cerca (store LanceDB, locale)
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
| *(nuova)* Profilo di ciascun Papa per argomenti | Temi naturali (topic) pesati **al netto del "dovuto"** da ruolo/liturgia; legame coi mandati dichiarati — vedi sotto |
| *(nuova)* Hanno rispettato il **mandato dichiarato** all'inizio? | Estrarre i temi dal discorso programmatico (inizio pontificato / primo saluto) e tracciarne il **trend per anno** lungo il pontificato — vedi sotto |

> Le tecniche sono indicazioni di metodo, non scelte definitive: si decideranno
> sui dati, strada facendo.

## Profilo di un Papa per argomenti (idea, ancora da mettere a fuoco)

Vorremmo dare a ciascun Papa un **profilo per argomenti**: di che cosa parla
*davvero*, e quanto. Il *come* e il *dove* non sono decisi (un campo in più nei
dati arricchiti? una vista nel repo di analisi?), ma la difficoltà vera è di
**metodo**, non di codice.

Il rischio è **misurare il calendario invece del Papa**. Tanti temi tornano *per
forza*, perché legati al **compito** e alla **liturgia**: Natale e Pasqua nelle
omelie, Maria all'Angelus, la pace negli auguri di inizio anno, i santi del
giorno nelle udienze. Sono temi **dovuti** dal ruolo, non scelti dalla persona:
sommarli a crudo darebbe a tutti i Papi lo stesso profilo "di base".

Il profilo interessante è quello che **resta togliendo il dovuto** — ciò che un
Papa aggiunge di suo: la sua **sensibilità**, o il **mandato che ha dichiarato**
(un programma di pontificato, un'enciclica che segna una linea). È il salto oltre
il `lift` per Papa del check dell'ingestion: non solo *"ne parla più degli
altri"*, ma *"ne parla più di quanto il suo ruolo e il calendario gli
imporrebbero"*.

Da decidere, strada facendo: come stimare la **baseline** del dovuto (confronto
fra Papi? un atteso per tipologia e periodo dell'anno?), e come legare i temi
emersi (topic) ai **mandati dichiarati** dei pontificati.

### Temi da aggiungere (e come misurarli)

La piccola esplorazione in [`prove/esplora_temi.py`](prove/esplora_temi.py) gira
su una lista di temi a **parole chiave** ereditata dal check dell'ingestion. Un
primo sguardo suggerisce che è proprio lì — nei temi distintivi — che un Papa
"porta il suo". Ne mancano alcuni che vale la pena indagare: **valore della vita
umana**, **aborto**, **dignità/valore dell'uomo**, **intelligenza artificiale**,
**cambiamento della Chiesa**.

Due avvertenze, che dicono *come* vanno misurati:
- **a parole chiave si misurano male**: "valore della vita", "cambiamento della
  Chiesa", "dignità dell'uomo" si dicono in mille modi → è il caso da **topic
  emergenti / ricerca semantica** (il vector database), non da conteggio di
  stringhe. È la stessa lezione del check dell'ingestion.
- **alcuni temi non esistono per tutti nel tempo**: l'**IA** è argomento solo
  recente (Francesco, Leone); confrontare GP2 sull'IA non vuol dire niente. Il
  `lift` va calcolato **solo dove il tema poteva esserci**.

> ⚠️ E un limite del corpus: sembra che i Papi "rispettino quanto dicevano prima"
> di esserlo, ma questo **non lo possiamo verificare qui**. `ingestion` scarica
> solo i documenti *da Papa*: vediamo l'accento *dentro* il pontificato (coerente
> col mandato dichiarato), non un confronto prima/dopo. Per quello servirebbero i
> testi pre-pontificato (da cardinale) → altra raccolta dati, da valutare.

### Il mandato dichiarato e la sua tenuta nel tempo

Una versione **verificabile** della domanda sopra: il mandato non lo prendiamo da
prima (non l'abbiamo), ma dal **discorso programmatico** con cui ogni Papa, appena
eletto, dichiara la sua linea — l'**omelia di inizio pontificato** (e, prima
ancora, il **primo saluto / benedizione «Urbi et Orbi»** dalla loggia). È detto
*da Papa*, quindi confrontarlo con il resto del pontificato è legittimo.

I documenti ci sono: il primo saluto si trova col comando `vdb.py primo-saluto`
del vector database; le omelie di inizio pontificato sono in `data/<papa>/homilies/`
(es. JPII *"Non abbiate paura, aprite le porte a Cristo"*, 1978; Francesco sul
*custodire*, 2013).

Schema dell'analisi:
1. **Estrarre i temi dichiarati** in quel discorso (topic / ricerca semantica,
   non parole chiave — stessa lezione: "custodire il creato" ≠ stringa);
2. per ciascun tema-mandato, misurarne il **trend per anno** lungo tutto il
   pontificato (quota di documenti / intensità semantica nel tempo);
3. leggerlo come **tenuta del mandato**: i temi dichiarati all'inizio crescono,
   restano, o svaniscono? E quali temi *non* dichiarati emergono strada facendo?

Output naturale: una **serie temporale per Papa** dei suoi temi-mandato (con la
solita cautela sul "dovuto" da ruolo/liturgia). È un confronto *dentro* il
pontificato — quello che il corpus permette davvero.

## Forma delle analisi (da definire)

Non è ancora deciso *come* verranno fatte ed esposte le analisi. Le ipotesi
sul tavolo:

- analisi **one-shot** (script o notebook che producono un risultato);
- **dashboard** interattive;
- **data visualization** e grafici;
- **notebook** o documenti **markdown** narrativi.

Il racconto — quale storia raccontano i dati, e in che forma — è parte del
lavoro da fare, non un dato di partenza.

## Copyright e dati: la regola del repo

Vale qui come nell'ingestion e nel vector database, ed è il vincolo che tiene
tutto "senza problemi":

- **Si versiona solo il codice rilanciabile.** I dati (corpus, indice arricchito)
  restano locali e in `.gitignore`; si rigenerano dagli altri due repo.
- **Nessun testo reale nel repo.** I testi restano © Libreria Editrice Vaticana;
  l'uso è personale e di studio, con la fonte (`url`) sempre tracciata nei
  metadati.

Per il text mining questo vincolo combacia con la natura stessa del lavoro: qui
si producono **viste aggregate**, non i testi. Conteggi, trend nel tempo, topic,
distanze tra corpora, frequenze di frame: tutti **risultati derivati** che
sintetizzano il corpus senza riprodurlo. Le eventuali **citazioni puntuali**
(per il RAG o per illustrare un tema) restano brevi estratti con la fonte
indicata — non la ripubblicazione dei documenti. In altre parole, l'output
naturale del repo (aggregati e visualizzazioni) è già nella forma che rispetta
il copyright.

## Setup

Ambiente Python per le viste aggregate / notebook / data viz. Dettagli (conda e
venv) in [setup/README.md](setup/README.md).

```bash
conda env create -f setup/environment.yml && conda activate textmining-papi
# oppure: pip install -r requirements.txt
```

## Stato

Scaffold iniziale: solo le domande e la direzione, più l'ambiente di base. Il
codice delle analisi arriverà man mano che i dati arricchiti del vector database
saranno disponibili.
