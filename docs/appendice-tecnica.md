# Appendice tecnica — come ci arriviamo

Gli articoli raccontano le conclusioni senza gergo; qui c'è il *come*. Una sezione
per ogni affermazione, con il metodo in chiaro. Il codice completo, rieseguibile,
è nei notebook in [`../analisi/`](../analisi/) (indicati di volta in volta).

Una premessa che vale per tutto: **parole o significato?** Quasi tutte le analisi
lavorano sul **significato** delle frasi (gli *embedding*: ogni passaggio diventa
un vettore di numeri che ne cattura il senso, così "casa comune" e "ambiente"
risultano vicini anche senza parole in comune). Le **parole chiave** (regex)
compaiono in un solo punto — il conteggio dei temi — e lì stanno **accanto** agli
embedding, non al loro posto: servono da controllo trasparente. Quando i due
metodi concordano, la conclusione è solida; quando divergono, vince il
significato. Nessuna analisi usa **soglie** ("sopra X parla del tema"): le
similarità del modello non sono calibrate, quindi confrontiamo sempre *distribuzioni*
e *posizioni relative*, mai un taglio assoluto.

---

## 0. I dati

- **~25.000 documenti** dei quattro Papi (Giovanni Paolo II, Benedetto XVI,
  Francesco, Leone XIV), scaricati dal sito vaticano.
- Ogni documento è spezzato in **passaggi** da ~180 parole; si tolgono
  intestazioni e i saluti tradotti in altre lingue, per non sporcare i conteggi.
- Ogni passaggio è trasformato in **vettore di significato** con un modello
  multilingue (`multilingual-e5-base`), e archiviato in un indice interrogabile.
- In totale ~163.000 passaggi "di sostanza". *(Notebook: tutti; costruzione
  dell'indice nel repo del vector database.)*

## 1. «La linea rossa è ~l'80%» (struttura per famiglie)

→ articolo *Di cosa parlano davvero i Papi*, §"Di cosa è fatto un Papa". **Notebook
[`04-struttura-argomenti`](../analisi/04-struttura-argomenti.ipynb).**

Abbiamo descritto le sei famiglie (liturgia, fede e devozione, eventi, viaggi,
programma, attualità) con una **frase-ancora** ciascuna, e l'abbiamo trasformata
in vettore. Poi, per **ogni passaggio** dei discorsi, abbiamo guardato a quale
ancora somiglia di più (la più vicina fra le sei — nessuna soglia) e gli abbiamo
dato quella famiglia. Lavorando sui *passaggi* e non sui documenti interi, un
discorso risulta un **mix** (in media 1,83 famiglie a testa; il 56% ne tocca
almeno due). La percentuale di passaggi per famiglia, per Papa, dà la
composizione: «fede e devozione» + «liturgia» fanno ~80% per tutti. *Tutto a
embedding.*

## 2. «I temi dominanti sono uguali per tutti» e «Francesco accentua i poveri, ma il lavoro è di Wojtyła»

→ articolo *Di cosa parlano davvero i Papi*, §"La stessa voce" e §"E allora,
comunista?". **Notebook [`01-temi-per-papa`](../analisi/01-temi-per-papa.ipynb).**

Qui usiamo **i due metodi insieme**, ed è il punto in cui la domanda "regex o
embedding?" trova risposta:

- **A parole (regex):** per ogni tema una lista di radici (es. `pover|emarginat`,
  `lavorator|operai|sindacat`); contiamo la % di documenti con almeno un passaggio
  che le contiene.
- **A significato (embedding):** descriviamo il tema con una frase, misuriamo
  quanto ogni documento le si avvicina, e prendiamo i più vicini **in pari numero**
  ai positivi a parole (stesso volume, così confrontiamo distribuzioni e non
  soglie).

Il **`lift`** citato negli articoli è solo questo: quanto un Papa sta sopra (>1) o
sotto (<1) la **media dei quattro** su quel tema. I due metodi danno lo **stesso
quadro** (continuità sui temi dominanti; Francesco sopra su poveri/migranti;
lavoro/operai primo Giovanni Paolo II) — ed è questa concordanza la prova che il
risultato non dipende dal metodo scelto. Dove divergono in dettaglio (es. l'aborto,
che a parole premia GP2/Benedetto ma a significato riavvicina Francesco/Leone, che
lo dicono altrimenti) crediamo al **significato**.

## 3. «Ambiente: ne parlano tutti uguale, la firma è la frase»

→ articolo *Di cosa parlano davvero i Papi*, §"E allora, comunista?". **Notebook
[`01-temi-per-papa`](../analisi/01-temi-per-papa.ipynb) e
[`02-parole-vs-significato`](../analisi/02-parole-vs-significato.ipynb).**

La quota di documenti sull'ambiente è ~16–19% per tutti e quattro (a parole e a
significato concordano). La differenza di Francesco non è il *tema* ma la
**formula**: confrontando il conteggio della frase esatta "casa comune" con quello
del tema generale si vede che il tema è di tutti, l'espressione è sua.

## 4. «I temi che emergono da soli» (topic emergenti)

→ metodo di sfondo, citato in *Parole o significato* e in *Di cosa parlano* (§"nel
tempo"). **Notebook [`03-topic-emergenti`](../analisi/03-topic-emergenti.ipynb)** e
**[`07-argomenti-nel-tempo`](../analisi/07-argomenti-nel-tempo.ipynb).**

Senza dirgli noi i temi: raggruppiamo i documenti per **vicinanza di significato**
(algoritmo *KMeans* sui vettori) e diamo un nome a ogni gruppo con le parole che lo
caratterizzano (frequenti *dentro* il gruppo e rare *fra* i gruppi). Emergono da
soli la linea rossa liturgica, lo strato "dovuto" dal ruolo (vescovi, diplomatici,
accademie, viaggi) e le firme dei singoli — conferma indipendente di ciò che le
famiglie del §1 dicevano.

Il notebook 07 mette a punto la pipeline: (1) si **marca** ogni passaggio nelle 6
famiglie (campo `famiglia`, da `vdb.py arricchisci`); (2) si tiene il **non-core**
(fuori da liturgia e fede — il ~20% dove si gioca la differenza) e lo si
**raggruppa** con un KMeans condiviso tra i Papi; (3) a ogni gruppo si dà un nome
**leggibile** leggendone i passaggi rappresentativi (le parole grezze del TF-IDF
erano illeggibili). Poi quota per anno → heatmap: righe piene = continui, macchie =
a ondate, spesso ai cambi di Papa. Metà del non-core resta comunque istituzionale
(vescovi, udienze, viaggi) e il volume pende su Giovanni Paolo II.

## 5. «Hanno tenuto il mandato» (fedeltà nel tempo)

→ articolo *Hanno mantenuto le promesse?*. **Notebook
[`05-mandato`](../analisi/05-mandato.ipynb).**

Prendiamo l'**omelia di inizio pontificato** di ciascuno e ne facciamo il
**baricentro di significato** (la media dei vettori dei suoi passaggi): è il
"vettore-mandato". Poi, anno per anno, misuriamo quanto i documenti di
quell'anno gli somigliano in media. Una linea **piatta** = nessuna deriva. *Tutto
a embedding.* Da leggere la **pendenza** (assenza di deriva), non l'altezza: ogni
Papa è confrontato col *suo* mandato, e le similarità del modello stanno comunque
tutte alte (vedi §6).

## 6. Cosa NON facciamo, e i limiti

- **Niente soglie.** Solo confronti relativi e distribuzioni (le similarità non
  sono calibrate: vanno lette in relativo, non come voti assoluti).
- **Solo viste aggregate.** Percentuali, medie, andamenti — mai i testi, che
  restano © Libreria Editrice Vaticana.
- **Solo documenti da Papa.** Non i testi precedenti (da cardinale): misuriamo la
  coerenza *dentro* il pontificato, non un "prima/dopo".
- **La lente "famiglie" è grossa.** «Fede e devozione» attira quasi tutto: ottima
  per il quadro d'insieme, meno per le distinzioni fini (per quelle, i temi
  puntuali del §2 e i topic del §4).
- **Strumento giovane.** Qualche etichetta e qualche numero andranno affinati; la
  direzione, su tutte le domande, è però stabile.
