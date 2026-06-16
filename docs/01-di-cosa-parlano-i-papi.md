# Di cosa parlano i Papi

*Quello che dicono i giornali, messo a confronto con quello che dicono i loro testi
— quattro Papi, venticinquemila discorsi, contati.*

---

I giornali raccontano i Papi a modo loro. È una narrazione mediatica, e come ogni
narrazione sceglie: sceglie la sintesi, il tono, gli argomenti da mettere in prima
fila — spesso quelli più discutibili, quelli che fanno notizia. Il Papa finisce per
diventare una bandiera, piantata su due o tre temi scelti da fuori. Ma se invece dei
titoli si guardassero i suoi testi, dati alla mano?

Le domande sono quelle di sempre, quelle che vengono parlando tra amici, e per una
volta si possono misurare. Di cosa parlano, i Papi? C'è continuità tra l'uno e
l'altro? E su quello che è davvero loro — i temi moderni, l'attualità, al di là
della liturgia e della fede, di cui parlano *per mestiere* — come si espongono?
Wojtyła e Francesco sono distanti come si dice, l'uno anticomunista e l'altro
accusato del contrario? Il papa bavarese ha rotto con chi lo ha preceduto, ed è poi
così lontano da chi è venuto dopo? E Leone, è arrivato in sordina, o nel solco degli
altri?

Il materiale per rispondere c'è: circa **venticinquemila testi pubblici** dei quattro
Papi più recenti — Giovanni Paolo II, Benedetto XVI, Francesco, Leone XIV. Per ogni
tema, basta contare in quanti documenti compare.

## Quasi tutto è mestiere

La prima risposta è scomoda per chi cerca la notizia: gran parte di quello che dice
un Papa è il suo lavoro. Diviso il contenuto in sei famiglie — **liturgia** (la
Messa, i sacramenti, le feste dell'anno), **fede e devozione** (Dio, Cristo, Maria,
i santi, la preghiera), **eventi e ricorrenze** (udienze, anniversari, le visite dei
vescovi), **viaggi**, **programma del pontificato**, **attualità** (pace, migranti,
ambiente, lavoro) — e assegnato ogni passaggio alla famiglia più vicina per
significato, **tre passaggi su quattro finiscono in *fede e devozione*** (76%), un
altro 3% in *liturgia*.

> **Come, tecnicamente.** Ogni passaggio (~180 parole) diventa un vettore col modello
> `multilingual-e5-base`; il confronto col significato delle sei famiglie è un coseno,
> e vince la più vicina. Quel 76% va letto per quello che è: la famiglia "fede e
> devozione" è così ampia che quasi ogni frase religiosa le cade vicina. Non misura
> una scelta del Papa, misura il mestiere — ed è alto per tutti e quattro proprio
> perché è il mestiere.

![La composizione dei discorsi per famiglia](immagini/sintesi-struttura.png)

La parte che distingue un Papa dall'altro, quindi, non è quel grosso blocco dovuto al
ruolo: è il quinto che resta. È lì che vale la pena guardare.

## La voce di fondo è la stessa

Prima di cercare le differenze, però, la domanda secca: c'è continuità? Conviene
misurarla non sul blocco "mestiere", ma tema per tema, ognuno contato per conto suo.
I tre che dominano tornano quasi identici in tutti e quattro i pontificati: Dio e il
Vangelo compaiono nell'**85%** dei documenti (tra l'84 e l'88 dei quattro), la pace
intorno al **50%**, la famiglia intorno al **52%**.

> **Come, tecnicamente.** Ogni tema misurato in due modi e tenuto buono solo se
> concordano: *a parole* (radici cercate con regex, quota di documenti che le
> contengono) e *a significato* (i documenti più vicini al tema, in pari numero, per
> confrontare distribuzioni e non soglie). Sui temi dominanti i due metodi danno lo
> stesso quadro.

![I temi dominanti, misurati per significato](immagini/sintesi-continuita-significato.png)

Quote quasi uguali a quarant'anni di distanza, da Wojtyła a Leone: questa è la
continuità, ed è solida perché ogni tema regge da solo, senza appoggiarsi al blocco
generico di prima.

## Wojtyła e Francesco: il comunismo

È qui che il titolo di giornale si gioca tutto. Sui temi sociali Francesco effettivamente
calca più degli altri: parla di poveri nel **46%** dei suoi documenti contro il 33-36%
di Giovanni Paolo II e Benedetto, di migranti nel **12%** contro il 6%, di giustizia
sociale nel **10%** contro il 6%. È il suo timbro, e i numeri non lo nascondono.

![I temi sociali: dove Francesco calca, e dove no](immagini/sintesi-comunista.png)

Ma "comunista" non regge per due motivi, ed entrambi sono nel grafico. Primo: sono temi
piccoli accanto a Dio, pace e famiglia, e li tratta anche chi comunista non era — è la
dottrina sociale della Chiesa, vecchia di oltre un secolo. Secondo, la riga del lavoro e
degli operai ribalta la storia: il primo è **Giovanni Paolo II**, al 12% dei suoi
documenti contro l'8% di Francesco — proprio il Papa che il comunismo ha contribuito a
farlo cadere. La distanza Wojtyła-Francesco, sull'asse "destra-sinistra" dei giornali,
non c'è: cambiano gli accenti dentro la stessa dottrina. Lo stesso vale per l'ambiente,
che tutti e quattro toccano tra il 16% e il 19%: di Francesco è la formula "casa comune"
della *Laudato si'*, non il tema.

## Benedetto ha rotto? Leone è in sordina?

Restano i due Papi che la narrazione tratta agli estremi: Benedetto il teologo che
"frena", Leone l'ultimo arrivato di cui non si sa nulla. I testi dicono altro.

Benedetto non rompe con niente: i suoi temi dominanti sono allineati agli altri (Dio e
Vangelo all'88%, famiglia al 55%, pace al 51%), e l'unica famiglia su cui spicca un po'
è *programma e storia* (6,7% contro il 5% degli altri) — coerente con un pontificato di
impronta dottrinale, non con una frattura. Leone, dal canto suo, in sordina non è: nel
suo (ancora breve) corpus la **pace** arriva al **70%** dei documenti, contro il ~50%
degli altri tre, e l'**intelligenza artificiale** compare nel **7,8%** — un tema che in
Giovanni Paolo II e Benedetto era a zero perché semplicemente non esisteva. Leone non
arriva piano: arriva nel solco dei predecessori, con un paio di accenti suoi.

> **Come, tecnicamente.** Tolto il blocco "mestiere" (liturgia e fede), il resto dei
> passaggi è raggruppato per significato in argomenti, ognuno con un nome dato leggendone
> i testi tipici, e contato anno per anno. La heatmap qui sotto: una riga per argomento,
> una colonna per anno, più scuro = se ne parla di più; le righe azzurre sono i cambi di
> Papa.

![Gli argomenti, oltre liturgia e fede, nel tempo](immagini/argomenti-nel-tempo.png)

Nel tempo si vede la stessa cosa: il fondo non si muove, gli accenti sì, e quasi sempre
al cambio di Papa. Le visite ai vescovi e la Polonia sono fitte negli anni di Wojtyła e
si schiariscono dopo; povertà e lavoro, fame e agricoltura, e il registro "a braccio" di
Francesco — interviste, dialoghi — si accendono dal 2013 e restano con Leone. Metà di
questi argomenti, va detto, è comunque istituzionale (vescovi, udienze, viaggi), e il
grosso del testo è di Wojtyła, che ha scritto molto più degli altri: contano le quote,
non i numeri secchi.

## Cosa resta

Tolti i titoli, resta un quadro semplice. La voce di fondo — Dio, la pace, la famiglia —
è la stessa per tutti e quattro, a decenni di distanza. Le differenze stanno negli
accenti, nel quinto di contenuto che ogni Papa aggiunge di suo, e si spostano col tempo
più che separare un Papa dagli altri. Francesco calca sui poveri, ma sul lavoro lo
precede Wojtyła; Benedetto non rompe; Leone non arriva in sordina. La bandiera che i
giornali piantano su un tema solo, alla prova dei testi, non sta in piedi.

---

*Solo conteggi e percentuali, mai i testi (© Libreria Editrice Vaticana). Il "come" di
ogni numero, passo per passo, è nell'[appendice tecnica](appendice-tecnica.md), che
porta ai notebook col codice.*
