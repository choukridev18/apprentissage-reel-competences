# Campagnes de tests QA

Portfolio QA — **Choukri**

API (Postman, pytest) · IHM (Playwright + Page Object) · SQL · JMeter · GitHub Actions (CI/CD)

Page déployée : [choukridev18.github.io/apprentissage-reel-competences](https://choukridev18.github.io/apprentissage-reel-competences/)

## Ce que j’ai testé

| Campagne | Outil | Preuve |
|----------|--------|--------|
| API (GET/POST/PUT/PATCH/DELETE, 401, Bearer) | Postman + pytest | `QA avance.postman_collection.json`, `test_echo.py` |
| IHM TodoMVC (ajouter, cocher, filtres, compteur) | Playwright, Page Object | `test_ihm_todo.py`, `pages/todo_page.py` |
| Charge API echo | JMeter | `charge_api_echo.jmx` |
| Contrôles base (orphelins, totaux, JOIN) | SQL | `exercice.sql`, schéma dans `sql_qa.md` |
| Anomalie + recette | rédaction | `bug_todo_ajouter.txt`, `rapport_recette.md` |
| Pipeline | GitHub Actions | `.github/workflows/ci.yml` : pytest API, puis Pages si vert |

La CI lance **`pytest test_echo.py`**. Les tests IHM se lancent en local (voir plus bas).

## Lancer

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest test_echo.py -q
pytest test_ihm_todo.py -q
```

SQL (jeu `qa_training.db` du dossier d’entraînement à côté de ce repo) :

```bash
sqlite3 ../entrainement_sql_python/data/qa_training.db < exercice.sql
```

## Recette TodoMVC

Périmètre : [demo.playwright.dev/todomvc](https://demo.playwright.dev/todomvc).  
Avis : **non livrable** — ajouter une tâche KO (ticket `bug_todo_ajouter.txt`).
