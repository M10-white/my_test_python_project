# Travaux Pratiques - TP1 et TP2

Ce dépôt contient les travaux pratiques réalisés dans le cadre du cours de développement :

```
.
├── .github/
│   └── workflows/
│       └── python-ci.yml     # Configuration GitHub Actions CI/CD
├── TP1/                      # TP1 : Tests unitaires (Python + PyTest)
│   ├── fonctions.py          # Implémentation des fonctions à tester
│   ├── test_fonctions.py     # Tests unitaires PyTest pour TP1
│   ├── 1er_Test_Success.png  # Capture d'écran des tests réussis
│   └── 2eme_Test_Success.png
├── TP2/                      # TP2 : Pipeline CI/CD avec GitHub Actions
│   ├── main.py               # Implémentation de la fonction `hello`
│   ├── test_main.py          # Tests unitaires PyTest pour TP2
│   ├── requirements.txt      # Dépendances du projet
│   ├── .flake8                # Configuration Flake8
│   ├── 1er_TestGitHubAction.png  # Capture d'écran CI/CD réussi
│   └── 1er_Test_Error.png
└── README.md                 # Ce fichier
  ```

## TP1 - Tests unitaires

**Dossier :** `TP1/`
**Objectif :** Implémenter et tester trois fonctions avec PyTest.
**Fichiers principaux :**
  - `fonctions.py`
  - `test_fonctions.py`
**Pour exécuter :**
  ```bash
  cd TP1
  pytest test_fonctions.py
  ```

## TP2 - Pipeline CI/CD avec GitHub Actions

**Dossier :** `TP2/`
**Objectif :** Mettre en place un workflow CI/CD avec GitHub Actions pour exécuter les tests et le linter.
**Configuration CI :** `.github/workflows/python-ci.yml`
**Fichiers principaux :**
  - `main.py`
  - `test_main.py`
  - `requirements.txt`
  - `.flake8`
**Pour exécuter localement :**
  ```bash
  cd TP2
  pip install -r requirements.txt
  pytest
  flake8 TP2/
  ```

## CI/CD (GitHub Actions)

Chaque push/pull request déclenche un pipeline défini dans `.github/workflows/python-ci.yml`.
Le pipeline :
  1. Checkout du code
  2. Installation de Python et des dépendances
  3. Exécution des tests PyTest
  4. Exécution de Flake8 pour la qualité du code

---

*Date : 12/05/2025*  
*Étudiant : Brahim C.*
