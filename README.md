# 🗺️ AI-Intelligent Location
### Retail Location Intelligence Agent — Rende (CS)

> Progetto di **AI Data Science** che analizza la distribuzione commerciale di Rende (Cosenza) usando clustering spaziale e intelligenza artificiale generativa per identificare le zone migliori dove aprire un nuovo punto vendita.

---

## 📌 Descrizione

Questo progetto implementa una **pipeline end-to-end di Location Intelligence** applicata al territorio di Rende (CS):

1. **Data Preparation** — dataset di 37 punti di interesse commerciali con coordinate GPS e affluenza giornaliera
2. **Spatial Clustering** — algoritmo DBSCAN per identificare automaticamente le zone commerciali
3. **Visualizzazione** — mappa interattiva con Folium che mostra i cluster per quartiere
4. **AI Agent** — integrazione con Claude API (Anthropic) per generare insight e raccomandazioni strategiche in autonomia

---

## 🛠️ Tecnologie

| Tecnologia | Utilizzo |
|-----------|---------|
| `Python` | Linguaggio principale |
| `Pandas` | Data preparation e analisi |
| `Scikit-learn` | Algoritmo DBSCAN per spatial clustering |
| `Folium` | Visualizzazione mappa interattiva |
| `Anthropic Claude API` | Generazione automatica di insight con AI |
| `Google Colab` | Ambiente cloud di sviluppo |

---

## 📁 Struttura del progetto

```
AI-Intelligent-Location/
│
├── main.py              # Pipeline completa — dalla preparazione dati al report AI
├── mappa_rende.html     # Mappa interattiva dei cluster commerciali
├── report_rende.md      # Report generato autonomamente dall'AI Agent
└── README.md            # Documentazione del progetto
```

---

## 🚀 Come eseguire

### 1. Apri su Google Colab
Carica `main.py` su [Google Colab](https://colab.research.google.com)

### 2. Installa le dipendenze
```python
!pip install geopandas folium anthropic plotly scikit-learn -q
```

### 3. Configura la API key
Vai su **Secrets** (icona 🔑 nel menu a sinistra di Colab) e aggiungi:
- **Nome:** `ANTHROPIC_API_KEY`
- **Valore:** la tua chiave da [console.anthropic.com](https://console.anthropic.com)

### 4. Esegui il codice
Lancia `main.py` — genererà automaticamente la mappa e il report AI.

---

## 📊 Risultati

Il clustering DBSCAN ha identificato **6 zone commerciali** su Rende:

| Cluster | Quartiere | Negozi | Affluenza media |
|---------|-----------|--------|----------------|
| 0 | Centro | 4 | 201 pax/giorno |
| 1 | Centro | 5 | 119 pax/giorno |
| 2 | Quattromiglia | 4 | 310 pax/giorno |
| 3 | Quattromiglia ⭐ | 10 | 520 pax/giorno |
| 4 | Quattromiglia | 3 | 317 pax/giorno |
| Outlier | Varie zone | 11 | — |

> ⭐ Il **Cluster 3 (Quattromiglia)** è il polo commerciale principale con la massima affluenza e densità di negozi.

---

## 🤖 AI Agent

Il cuore del progetto è un agente AI che:

- Riceve i dati dei cluster come input
- Li analizza autonomamente tramite **Claude API** di Anthropic
- Genera un report professionale con analisi per zona, gap commerciali e raccomandazioni strategiche

Questo approccio è in linea con i pattern di **Agentic AI** descritti nei requisiti di posizioni avanzate di Data Science: agenti capaci di interrogare dataset, generare insight e orchestrare step analitici in autonomia.

---

## 🔮 Sviluppi futuri

- Integrazione con dati reali di mobilità da operatori telco
- Deploy su cloud (Azure / Google Vertex AI)
- Network analysis per ottimizzare la distribuzione commerciale
- Modello predittivo di domanda per zona geografica
- Orchestrazione multi-agente con LangChain / LangGraph

---

## 👤 Autore

**Cristian Clausi**
Neolaureato in Ingegneria Gestionale — specializzazione Sostenibilità
