# Compétences — Choukri (apprentissage)

Ce que tu peux **dire** en entretien. Pas Cypress, pas Gherkin, pas Robot, pas certif ISTQB Generative AI, pas assistant LLM.

Repo : [qa-campagnes](https://github.com/choukridev18/qa-campagnes)

## QA (campagnes)

- API : Postman + pytest (`test_echo.py`) — 200/401, Bearer, assertions
- IHM : Playwright + Page Object (`pages/todo_page.py`)
- Charge : JMeter (Thread Group, ramp-up, 90 % Line = 90 % des **échantillons**)
- SQL : JOIN, orphelin `LEFT` + `WHERE users.id IS NULL`, contrôle vs API
- Git / GitHub / CI-CD : `ci.yml` (`pytest` puis Pages si `needs: tests` vert)
- Rédaction : cas de test, bug (`bug_todo_ajouter.txt`), recette

## ISTQB / process (gros)

- Fonctionnel vs non fonctionnel (JMeter = non fonc.)
- Erreur / défaut / bug
- Vérif (contrat) vs valid (métier / PO)
- 4 niveaux ; régression ; smoke
- Scénario = quoi, cas = comment, ticket = signaler
- Plan : périmètre, comment, env, qui
- Agile vs classique ; planning / daily / review / rétro ; REX
- Valeurs limites : règle ≥ 18 → **17** et **18**

## IA générative pour le test (socle 2026-11-13)

- Prompt **3 blocs** : contexte (URL, Swagger/AC) → commande → limites d’outil
- L’IA **écrit** des idées dans le **chat** ; elle **n’exécute pas** (Send / pytest = toi)
- Déjà les cas en tête → **direct** Postman
- **Hallucination** : a l’air vrai, faux après verif
- **Biais** : elle reste sur les 200 ; tu redemandes l’erreur (401)
- Pas coller : token, mot de passe, emails / données **prod** ; jeux **@example.com**
- US floue : toi tu signales, PO **tranche** ; l’IA liste les lectures
- Ticket : l’IA = squelette ; **obtenu** = toi
- POM : coller **quelques lignes** à relire, pas régénérer la classe ; puis pytest
- L’IA **s’ajoute** au plan de test, elle **n’est pas** le plan

- **LLM** : programme qui **devine la suite** du texte / du code (ChatGPT, Tab Postman « // 200 »)
- **Chat** : l’échange utilisateur ↔ IA
- **Assistant de test** : même **boucle** automatisée (LLM + outils). Toi tu la fais **à la main** : chat → outil → verif → chat. Souvent **flaky** si c’est un robot. Tu ne **vends** pas un assistant.
- **Flaky** : résultat **pas stable**, sans vrai nouveau bug

Phrase entretien : *« L’IA accélère le brouillon. Je vérifie. Le test, c’est moi. Je ne vends pas un robot QA. »*
