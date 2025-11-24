#  Cahier des charges — Projet Spotify : Prédiction de Genre Musical

## 1. Contexte du projet
Ce projet vise à prédire le **genre musical** d’un morceau à partir de ses **features audio** fournies par Spotify.  
Il s’inscrit dans un projet académique où plusieurs approches de Machine Learning doivent être testées et comparées.

---

## 2. Objectifs

### Objectif principal
Développer un modèle capable de prévoir le **genre musical** à partir d’un ensemble de caractéristiques audio.

### Objectifs secondaires
- Explorer et analyser le dataset.
- Réaliser un prétraitement complet et reproductible.
- Tester au moins **4 méthodes de prédiction** :
  - Une méthode interprétable.
  - Une méthode ensembliste.
  - Une méthode basée sur un réseau de neurones.
  - Une quatrième méthode libre.
- Comparer objectivement les performances des modèles.
- Organiser le projet de manière professionnelle (VS Code, GitHub, notebooks propres, etc.).

---

## 3. Architecture du projet
spotify-genre-project/
├─ Data/
│ ├─ dataset.csv
│ └─ processed/
├─ notebooks/
│ ├─ 01_exploration.ipynb
│ ├─ 02_preprocessing.ipynb
│ └─ 03_modelisation.ipynb
├─ reports/
│ ├─ figures/
│ └─ results.md
├─ src/
│ ├─ preprocessing.py
│ ├─ models.py
│ ├─ evaluation.py
│ └─ utils.py
├─ models_saved/
├─ README.md
├─ requirements.txt
└─ .gitignore


---

## 4. Prétraitement des données

Le prétraitement comprendra les étapes suivantes :
1. Chargement du dataset brut.
2. Nettoyage des données :
   - gestion des valeurs manquantes ;
   - détection de valeurs aberrantes (optionnel) ;
   - normalisation / standardisation.
3. Sélection des variables pertinentes.
4. Encodage de la cible (genre).
5. Séparation en jeux d’entraînement et de test.
6. Export des données prétraitées dans `Data/processed/`.

---

## 5. Méthodes de prédiction

### Méthodes exigées

#### 1. Méthode interprétable
Exemples :
- Régression Logistique  
- Arbre de Décision

#### 2. Méthode ensembliste
Exemples :
- Random Forest  
- Gradient Boosting  
- XGBoost / LightGBM (optionnel)

#### 3. Méthode basée sur un réseau de neurones
Exemples :
- MLPClassifier (scikit-learn)
- MLP en Keras ou PyTorch

#### 4. Méthode libre
Exemples :
- SVM  
- k-NN  
- Naive Bayes  

Chaque modèle sera défini dans `src/models.py` et entraîné depuis le notebook `03_modelisation.ipynb`.

---

## 6. Critères d’évaluation des modèles

Les modèles seront comparés selon :
- **Accuracy**
- **F1-score macro**
- Matrice de confusion
- Temps d’entraînement (optionnel)
- Robustesse des résultats (optionnel)

Les résultats seront consolidés dans `reports/results.md`.

---

## 7. Visualisations demandées

Les visualisations minimales incluent :
- Histogrammes et boxplots des features audio.
- Heatmap de corrélation.
- Répartition des genres.
- Importance des variables (pour Random Forest, Logistic Regression).
- Matrices de confusion pour chaque modèle.

Les figures seront stockées dans `reports/figures/`.

---

## 8. Technologies et librairies utilisées

- Python 3.x  
- VS Code / Jupyter  
- pandas, numpy  
- scikit-learn  
- matplotlib, seaborn  
- TensorFlow / PyTorch (optionnel)  
- Git & GitHub  

---

## 9. Reproductibilité

- Création d’un fichier `requirements.txt` listant les librairies nécessaires.
- Structure du projet modulable via le dossier `src/`.
- Code compatible Google Colab.
- Notebooks propres et entièrement exécutables.

---

## 10. Collaboration

- Gestion du versioning avec GitHub.
- README complet contenant :
  - instructions d’installation ;
  - présentation du dataset ;
  - description des modèles ;
  - résultats synthétiques.
- Commentaires clairs et code documenté.

---

## 11. Livrables

- Repository GitHub complet et propre.
- Notebooks :
  - `01_exploration.ipynb`
  - `02_preprocessing.ipynb`
  - `03_modelisation.ipynb`
- Dossier `src/` fonctionnel.
- Résultats comparatifs (`reports/results.md`).
- Graphiques en haute qualité dans `reports/figures/`.
- Modèles entraînés (`models_saved/`).
- README documenté.

---

