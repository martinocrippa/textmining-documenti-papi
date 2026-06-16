# Di cosa parlano davvero i Papi

*Abbiamo preso venticinquemila discorsi di quattro Papi e li abbiamo contati. Per
rispondere, una buona volta, alle domande che ci si fa tra amici — una tira
l'altra.*

---

Su Papa Francesco c'è una narrazione precisa — quella dei giornali, quella che
torna quando se ne parla tra amici: *"ma è comunista? Ha rotto con quelli di prima?
Parla solo di migranti?"*. Domande vere. Solo che la risposta, di solito, è
un'impressione. E lato dati, invece, è davvero così? Per scoprirlo abbiamo fatto la
cosa più semplice: **guardiamo i dati**.

Abbiamo raccolto circa **venticinquemila testi** dei quattro Papi più recenti —
Giovanni Paolo II, Benedetto XVI, Francesco e Leone XIV — e li abbiamo fatti
leggere a un programma capace non solo di cercare le parole, ma di capire il
**senso** delle frasi. Poi abbiamo seguito le domande, una alla volta, lasciando
che ogni risposta ne aprisse un'altra.

Con una regola fissa, per non prenderci in giro: a ogni domanda **cambiamo
strumento di misura** — prima le parole, poi il significato, poi i gruppi che
emergono da soli — e una risposta la teniamo buona solo se gli strumenti diversi
**dicono lo stesso numero**. Se concordano, ci fidiamo; se litigano, è un segnale
che lì sotto c'è qualcosa da guardare meglio.

## Prima domanda: di cosa è fatto un Papa?

**La domanda.** Se prendi *tutto* quello che dice un Papa, di che cosa è fatto,
davvero?

**In numeri.** Abbiamo descritto sei grandi famiglie di argomenti (liturgia; fede
e devozione; gli eventi che gli organizzano; i viaggi; il programma del
pontificato; l'attualità) e poi, per **significato**, abbiamo assegnato ogni
*passaggio* dei discorsi alla famiglia più affine. Non i discorsi interi: i pezzi
— perché un'omelia mischia liturgia e attualità nella stessa pagina.[^struttura]

> **Come, tecnicamente.** Ogni passaggio (~180 parole) diventa un *vettore* di
> significato con il modello multilingue `multilingual-e5-base`. I vettori sono
> normalizzati, quindi confrontarli è calcolare un **coseno**: misuriamo il
> passaggio contro sei "frasi-ancora" (una per famiglia) e gli diamo la **più
> vicina**. Per significato, non per parole; e **nessuna soglia** — solo "qual è
> l'ancora più vicina".

**La risposta.** Circa l'**80% di tutto è la stessa cosa**, per tutti e quattro:
Dio, Gesù, Maria, il Vangelo, i sacramenti — la *lunga linea rossa*. I temi "da
prima pagina" vivono nel **20% che resta**.

![Di cosa parlano: la struttura per famiglie](immagini/sintesi-struttura.png)

**È la nostra vista o è nel dato?** Le sei famiglie, va detto, sono pur sempre una
*nostra* ipotesi: le proponiamo noi e ci misuriamo i testi. Allora abbiamo fatto
la controprova opposta — lasciare che gli argomenti **emergano dai testi**,
raggruppandoli per conto loro, senza suggerirne nessuno. E tornano le stesse
grandi aree: il fondo liturgico-devozionale, poi viaggi, eventi, programma,
attualità — con in più qualche dettaglio fine (le visite dei vescovi, la Settimana
Santa, il dialogo tra religioni). La nostra **vista** e il **dato** si danno
ragione a vicenda.[^dato]

> **Come, tecnicamente.** Due strade opposte, stesso punto d'arrivo: o *proponiamo*
> noi le sei famiglie-ancora e assegniamo ogni discorso alla più vicina (la nostra
> ipotesi); o lasciamo che un **KMeans** sui vettori e5 *raggruppi* i discorsi
> simili e faccia emergere gli argomenti da sé, etichettati con le parole che li
> caratterizzano (c-TF-IDF: frequenti *nel* gruppo, rare *fra* i gruppi — il dato).
> Quando le due strade convergono, ci si può fidare.

**La domanda che ne nasce.** Ma se il fondo è identico per tutti, allora dov'è
finita la "rottura" di cui si parla sempre con Francesco?

## Seconda domanda: continuità o rottura?

**La domanda.** I temi portanti sono gli stessi da un pontificato all'altro, o
Francesco ha davvero cambiato musica?

**In numeri.** Qui non ci siamo fidati di un metodo solo. Abbiamo misurato i temi
dominanti **a significato** (il programma capisce il senso delle frasi) e
**ricontrollato a parole** (le parole chiave secche). E, come controprova, abbiamo
lasciato che i temi **emergessero da soli** dai testi, raggruppando i discorsi per
vicinanza di senso senza suggerirgliene nessuno.[^continuita]

> **Come, tecnicamente.** Tre lenti sulla stessa cosa. (1) *Parole chiave*: liste
> di radici via regex (es. `pover|emarginat`), si conta la quota di documenti che
> ne contengono almeno una. (2) *Significato*: lo stesso tema descritto a frase, si
> prendono i documenti più vicini (coseno sugli e5) **in pari numero** ai positivi
> a parole — stesso volume, così confrontiamo distribuzioni, non soglie. (3)
> *Raggruppamento* automatico (KMeans) senza temi imposti. Se tutte e tre dicono lo
> stesso, è solido.

**La risposta.** **Continuità schiacciante.** I temi che dominano — parlare di Dio
e del Vangelo, della pace, della famiglia — tornano quasi alle stesse percentuali
per tutti e quattro. E lo si vede da ogni angolazione: misurati a significato
(qui sotto), confermati a parole, e ritrovati quando i temi emergono da soli — i
gruppi più grandi, quelli liturgici e devozionali, ricorrono per **tutti**; solo i
gruppi piccoli portano una firma personale.[^topic] Su questo i Papi sono **la
stessa voce**: Francesco cambia gli accenti, non la sostanza.

![La continuità vista dagli embedding](immagini/sintesi-continuita-significato.png)

**La domanda che ne nasce.** E allora quell'idea — "è comunista" — da dove salta
fuori? Qualcosa di diverso, in Francesco, ci sarà pure.

## Terza domanda: Francesco è comunista?

**La domanda.** I poveri, i migranti, le disuguaglianze: sono *davvero* una sua
fissazione? E basta questo a fare di un Papa un comunista?

**In numeri.** Stesso conteggio dei temi, puntato sui temi "sociali" — poveri,
migranti, giustizia, lavoro — e confrontato fra i quattro.[^sociali]

> **Come, tecnicamente.** Lo stesso conteggio di prima (parole *e* significato),
> ristretto ai temi sociali. Per confrontare alla pari usiamo il **`lift`**: la
> quota di un Papa su quel tema divisa per la media dei quattro — >1 sta sopra la
> media, <1 sotto, ~1 in linea.

**La risposta.** Sì, Francesco **accentua** davvero poveri, migranti e
disuguaglianze: è il suo timbro. Ma due cose raddrizzano il titolo. Primo: sono
temi **minori** rispetto a Dio/pace/famiglia, e **li trattano tutti** — è la
dottrina sociale della Chiesa, vecchia di oltre un secolo. Secondo, la prova del
nove: guardate la colonna del **lavoro e degli operai**. Il primo non è Francesco
— è **Giovanni Paolo II**, il doppio degli altri. Cioè il Papa che ha contribuito
a far *cadere* il comunismo. Parlare di poveri non rende comunisti.

![Sui temi sociali: Francesco accentua, ma il lavoro è di Wojtyła](immagini/sintesi-comunista.png)

Stessa storia per l'ambiente: ne parlano tutti più o meno allo stesso modo. Quello
che è *davvero* di Francesco non è il tema, è il **modo di dirlo** — la formula
"casa comune" della *Laudato si'*.[^ambiente]

## E nel tempo? Il fondo resta, gli accenti si spostano

Un ultimo taglio, il più severo. Togliamo il fondo — liturgia, fede e devozione,
che già sappiamo continuo per tutti — e teniamo solo il resto: gli argomenti che
restano quando levi la parte dovuta dal ruolo. Quelli li lasciamo emergere dai
dati, gli diamo un nome leggendoli, e li contiamo anno per anno.

![Gli argomenti (oltre liturgia e fede) seguiti nel tempo](immagini/argomenti-nel-tempo.png)

> **Come, tecnicamente.** Si tengono i soli passaggi non liturgici e non
> devozionali, si raggruppano per significato (un KMeans condiviso tra i quattro
> Papi, così un argomento vale lo stesso per tutti) e a ogni gruppo si dà un nome
> leggendone i passaggi tipici. Poi: la quota di ogni argomento, anno per anno.

Si legge così: ogni riga è un argomento, ogni colonna un anno, più scuro vuol dire
che se ne è parlato di più; le righe azzurre sono i cambi di Papa.

Due avvertenze prima della storia. Anche qui metà degli argomenti è
**istituzionale** — visite dei vescovi, udienze, viaggi, diplomazia: roba dettata
dal ruolo, non scelta. E il grosso del testo è di Giovanni Paolo II, che ha scritto
molto più degli altri: contano le quote, non i numeri secchi.

Detto questo, gli argomenti di contenuto **si muovono, quasi sempre al cambio di
Papa**. Le visite *ad limina* e la Polonia sono fitte negli anni di Giovanni Paolo
II e si schiariscono dopo. **Povertà e lavoro**, **fame e agricoltura** (la FAO) e
il registro **"a braccio" di Francesco** — interviste, dialoghi — si accendono dal
2013 e restano con Leone. **Pace e disarmo** va a tratti, segue le guerre del
momento. Il fondo che abbiamo tolto, invece, non si muove: è la continuità degli
altri capitoli.[^tempo]

Una cautela: la heatmap dice *che* un argomento va a ondate, non ancora *cosa*
contiene di preciso quell'ondata. Per quello serve scendere nel dettaglio, una
macchia alla volta — lavoro per le analisi che verranno.

## Il prossimo passo: un profilo per ogni Papa

L'idea che vorremmo provare è semplice: dare a ciascun Papa un suo **profilo di
argomenti** — quanto pesa ognuno dei temi, in proporzione — e poi mettere i quattro
profili uno accanto all'altro, per leggere le differenze a colpo d'occhio invece
che frase per frase.

> **Come, tecnicamente.** Per ogni Papa un vettore di quote (un numero per
> argomento, che somma a 1: la sua composizione tematica). Il confronto a coppie con
> una distanza fra distribuzioni — coseno, oppure Jensen-Shannon — dice quanto due
> Papi si somigliano; l'intera matrice si può proiettare in due dimensioni per
> vederli su una mappa.

**Pro.** È onesto e leggibile: un solo quadro mette i quattro alla pari e fa vedere
*quanto* e *dove* si discostano, non solo "sì/no si somigliano". Si aggancia diretto
ai conteggi che abbiamo già, e regge la nostra regola — lo stesso profilo si può
rifare a parole, a significato e dai cluster, e confrontare i tre.

**Contro.** Il profilo dipende da *come* abbiamo tagliato gli argomenti: cluster
troppo scissi gonfiano le differenze, troppo grossi le nascondono — l'aggregato è
più affidabile del singolo gruppo. E un profilo medio appiattisce il tempo: due
Papi possono avere lo stesso profilo "totale" pur avendolo costruito in stagioni
diverse. Va quindi letto insieme alla heatmap, non al suo posto.

## La morale

Non volevamo dare addosso a nessuno: volevamo capire. E per capire abbiamo
cambiato lente di continuo — contare le parole, poi pesare il **significato**, poi
lasciare che gli argomenti **emergessero da soli** — e a ogni salto di tecnica
guardavamo se la risposta reggeva. Ha retto sempre. Da qualunque parte la guardi,
viene fuori la stessa cosa: non un Papa contro gli altri, ma una voce sola che
sposta accenti e parole su un filo che resta. In una riga:

> **Francesco cambia gli accenti, non la sostanza. Continuità piena, comunismo no.**

---

*Una nota onesta. Qui abbiamo guardato solo conteggi e percentuali, mai
ripubblicato i testi (sono dei loro autori). È uno strumento ancora giovane, e
qualche numero andrà limato — ma la direzione si vede, ed è solida.*

[^struttura]: Ogni *passaggio* è assegnato, **per significato** (embedding, non
per parole), alla più vicina fra sei famiglie-ancora; la quota di passaggi per
famiglia dà la composizione. La linea rossa = «fede e devozione» + «liturgia».
*Appendice tecnica*, §1.

[^continuita]: Temi dominanti misurati **a significato** e **a parole** (i due
concordano); il `lift` direbbe quanto un Papa sta sopra/sotto la media — qui è
~1 per tutti, cioè nessuno si stacca. *Appendice tecnica*, §2.

[^topic]: Controprova senza temi imposti: i discorsi sono raggruppati per
vicinanza di significato e i gruppi più grandi (liturgico-devozionali) compaiono
per tutti e quattro. *Appendice tecnica*, §4.

[^sociali]: Stesso conteggio del §2, sui temi sociali. Che il lavoro/operai sia
primo in Giovanni Paolo II vale **sia a parole sia a significato**. *Appendice
tecnica*, §2.

[^ambiente]: Quota di documenti sull'ambiente quasi identica per i quattro; la
differenza è la **frase** "casa comune", non il tema. *Appendice tecnica*, §3.

[^dato]: Controprova "dal dato": i discorsi sono raggruppati automaticamente per
significato, senza temi imposti, e gli argomenti emergono da soli — confermando le
famiglie proposte da noi. *Appendice tecnica*, §4.

[^tempo]: Pipeline: marcatura nelle 6 famiglie → si tiene il **non-core** (fuori da
liturgia e fede) → raggruppamento condiviso tra i Papi → nome a ogni gruppo
leggendone i passaggi tipici → quota per anno. *Appendice tecnica*, §4 e notebook 07.
