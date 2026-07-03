# Tension sur la ressource en eau, Bassins versants France

Carte interactive croisant l'intensité des sécheresses (VigiEau, 2019-2024) et le
volume d'eau prélevé (Hub'Eau/BNPE, moyenne 2019-2023) par bassin versant
topographique (SANDRE), pour la France métropolitaine.

Recherche par commune ou par bassin versant, situation actuelle en direct (API
VigiEau) au clic sur un bassin, et export des données au format CSV.

## Voir la carte

https://aleas-territoire.github.io/risko.V1/

## Contenu

- `index.html` : la web map (Leaflet + Leaflet.VectorGrid)
- `tiles/` : tuiles vectorielles MVT (zoom 5 à 9), générées avec [Tippecanoe](https://github.com/mapbox/tippecanoe)
- `bv_index.json`, `communes_index.json` : index de recherche (bassins versants, communes)
- `bassins_versants_tension_eau.csv` : export des données bivariées (téléchargeable depuis la carte)
- `logo_geopi.png` : logo Géopi
- `serve.py` : petit serveur local pour tester avant publication

## Sources

- Bassins versants topographiques : SANDRE / BD Topage
- Zones d'alerte sécheresse : SANDRE, service WFS `geo/zas`
- Prélèvements en eau : Hub'Eau (API BNPE), ministère de la Transition écologique
- Arrêtés de restriction sécheresse : VigiEau, data.gouv.fr
- Situation actuelle (temps réel) : API VigiEau (`api.vigieau.gouv.fr`)

## Méthodologie

Score sécheresse : pondération vigilance=1, alerte=2, alerte renforcée=4, crise=8,
multipliée par la durée en jours, plafonnée à 60 points/mois/zone, normalisée sur 100
sur la période 2019-2024 (72 mois). Classification en tercile sur les bassins à score
strictement positif.

Prélèvement : moyenne annuelle du volume prélevé 2019-2023 par commune, agrégée par
bassin versant (jointure spatiale centroïde). Classification en tercile sur le rang
percentile national.

## Réalisation

Webmap réalisée par Josselin Thonnelier pour [Géopi](https://aleas-territoire.github.io/geopi/) (2026).
