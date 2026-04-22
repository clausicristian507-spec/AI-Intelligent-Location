# RETAIL LOCATION INTELLIGENCE AGENT — RENDE (CS)
# Progetto AI per analisi commerciale del territorio
# Author: Cristian Clausi
#
# SETUP: Prima di eseguire, aggiungi la tua API key nei Secrets di Colab
# con il nome: ANTHROPIC_API_KEY

# ============================================================
# 1. INSTALLAZIONE LIBRERIE
# ============================================================
# !pip install geopandas folium anthropic plotly scikit-learn -q

# ============================================================
# 2. IMPORT
# ============================================================
import pandas as pd
import numpy as np
import folium
from sklearn.cluster import DBSCAN
import anthropic
from google.colab import userdata

# ============================================================
# 3. DATASET — Punti di interesse commerciali di Rende (CS)
# ============================================================
import numpy as np
np.random.seed(42)

negozi = {
    "nome": [
        "Supermercato Conad Centro", "Bar Centrale", "Farmacia Rende",
        "Pizzeria da Mario", "Abbigliamento Moda", "Tabacchi Centro",
        "Ristorante Calabria", "Panetteria Tradizione",
        "McDonald s Quattromiglia", "Bar Universita", "Supermercato Lidl",
        "Pizzeria Quattromiglia", "Farmacia Universitaria", "Caffe dello Studente",
        "Ristorante Pizzeria", "Abbigliamento Jeans", "Tabacchi Quattromiglia",
        "Kebab Express", "Libreria Universitaria", "Gelateria Quattromiglia",
        "Centro Commerciale Roges", "Zara Roges", "H&M Roges",
        "Supermercato Eurospin", "McDonald s Roges", "Burger King",
        "Ottica Roges", "Gioielleria Roges", "Profumeria Douglas",
        "Scarpe e Scarpe", "Elettronica Expert",
        "Bar Commenda", "Farmacia Commenda", "Pizzeria Commenda",
        "Supermercato Dok", "Parrucchiere Style", "Estetista Beauty",
    ],
    "tipo": [
        "supermercato", "bar", "farmacia", "ristorante", "abbigliamento",
        "tabacchi", "ristorante", "panetteria",
        "fast_food", "bar", "supermercato", "ristorante", "farmacia",
        "bar", "ristorante", "abbigliamento", "tabacchi", "fast_food",
        "libreria", "gelateria",
        "centro_commerciale", "abbigliamento", "abbigliamento", "supermercato",
        "fast_food", "fast_food", "ottica", "gioielleria", "profumeria",
        "scarpe", "elettronica",
        "bar", "farmacia", "ristorante", "supermercato", "parrucchiere", "estetica"
    ],
    "quartiere": [
        "Centro", "Centro", "Centro", "Centro", "Centro", "Centro", "Centro", "Centro",
        "Quattromiglia", "Quattromiglia", "Quattromiglia", "Quattromiglia", "Quattromiglia",
        "Quattromiglia", "Quattromiglia", "Quattromiglia", "Quattromiglia", "Quattromiglia",
        "Quattromiglia", "Quattromiglia",
        "Roges", "Roges", "Roges", "Roges", "Roges", "Roges", "Roges", "Roges",
        "Roges", "Roges", "Roges",
        "Commenda", "Commenda", "Commenda", "Commenda", "Commenda", "Commenda"
    ],
    "lat": (
        np.random.normal(39.3516, 0.003, 8).tolist() +
        np.random.normal(39.3400, 0.004, 12).tolist() +
        np.random.normal(39.3450, 0.003, 11).tolist() +
        np.random.normal(39.3480, 0.003, 6).tolist()
    ),
    "lon": (
        np.random.normal(16.1800, 0.003, 8).tolist() +
        np.random.normal(16.1950, 0.004, 12).tolist() +
        np.random.normal(16.1850, 0.003, 11).tolist() +
        np.random.normal(16.1750, 0.003, 6).tolist()
    ),
    "affluenza_giornaliera": (
        np.random.randint(50, 300, 8).tolist() +
        np.random.randint(100, 500, 12).tolist() +
        np.random.randint(200, 800, 11).tolist() +
        np.random.randint(50, 250, 6).tolist()
    )
}

df = pd.DataFrame(negozi)
print(f"Dataset: {len(df)} punti di interesse")

# ============================================================
# 4. CLUSTERING DBSCAN
# ============================================================
coords = df[["lat", "lon"]].values
dbscan = DBSCAN(eps=0.003, min_samples=3, metric="euclidean")
df["cluster"] = dbscan.fit_predict(coords)

n_clusters = len(set(df["cluster"])) - (1 if -1 in df["cluster"] else 0)
print(f"Cluster trovati: {n_clusters}")

# ============================================================
# 5. MAPPA INTERATTIVA
# ============================================================
colori_cluster = {-1:"gray", 0:"blue", 1:"green", 2:"red", 3:"orange", 4:"purple", 5:"darkred"}

mappa = folium.Map(location=[39.3480, 16.1850], zoom_start=14, tiles="CartoDB positron")

for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=8,
        color=colori_cluster.get(row["cluster"], "gray"),
        fill=True,
        fill_opacity=0.8,
        tooltip=f"Cluster {row[chr(99)+chr(108)+chr(117)+chr(115)+chr(116)+chr(101)+chr(114)]} | {row[chr(110)+chr(111)+chr(109)+chr(101)]} | {row[chr(97)+chr(102)+chr(102)+chr(108)+chr(117)+chr(101)+chr(110)+chr(122)+chr(97)+chr(95)+chr(103)+chr(105)+chr(111)+chr(114)+chr(110)+chr(97)+chr(108)+chr(105)+chr(101)+chr(114)+chr(97)]} persone/giorno"
    ).add_to(mappa)

mappa.save("mappa_rende.html")
print("Mappa salvata!")

# ============================================================
# 6. AGENTE AI — Report generato da Claude
# ============================================================
client = anthropic.Anthropic(api_key=userdata.get("ANTHROPIC_API_KEY"))

cluster_stats = df.groupby("cluster").agg(
    n_negozi=("nome", "count"),
    affluenza_media=("affluenza_giornaliera", "mean"),
    quartiere=("quartiere", "first"),
    tipi=("tipo", lambda x: ", ".join(x.unique()))
).round(0)

prompt = f"""
Sei un esperto di Location Intelligence e Retail Analytics.
Hai analizzato i dati commerciali della citta di Rende (Cosenza, Calabria).

Risultati clustering DBSCAN:
{cluster_stats.to_string()}

Outlier: {len(df[df["cluster"] == -1])} negozi isolati.

Genera un report professionale con:
1. Analisi di ogni cluster
2. Gap commerciali identificati
3. Raccomandazione strategica su dove aprire un nuovo punto vendita
4. Prossimi passi analitici

Italiano, tono professionale, max 400 parole.
"""

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=600,
    messages=[{"role": "user", "content": prompt}]
)

report = message.content[0].text

with open("report_rende.md", "w", encoding="utf-8") as f:
    f.write("# Retail Location Intelligence Report — Rende (CS)\n\n")
    f.write(report)

print("Report AI generato!")
print(report)
