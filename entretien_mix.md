# Entretien mix QA

Sources : tes notes (réunions, ISTQB, outils) + ce repo (`ci.yml`, `exercice.sql`, Playwright).

**Règle :** expliquer **en gros**. Pas une phrase apprise. Pas de QCM. Une question à la fois dans le chat.

Hors cadre ici : Docker, OAuth, mocks Python, XPath de 10 étages.

---

## YAML

1. À quoi sert un fichier `.yml` / `.yaml` ? Dans ce projet, à quoi sert `.github/workflows/ci.yml` ?
2. Le job `deploy` a `needs: tests`. Ça veut dire quoi si pytest est rouge ?

## ISTQB (gros)

3. Test **fonctionnel** vs **non fonctionnel**. Un exemple de chaque, avec tes outils (Postman / Playwright / JMeter).
4. **Erreur**, **défaut**, **bug** — la différence.
5. **Vérification** vs **validation**.
6. Les **4 niveaux** de test (unitaire, intégration, système, acceptation) — qui fait quoi, en gros.
7. Test de **régression** : à quoi ça sert.
8. **Cas de test** vs **scénario** vs **ticket de bug**.
9. Un **plan de test** contient quoi (3–4 points, pas la liste par cœur).
10. Test **smoke** : quand, et quoi.

## SQL

11. Clé **primaire** vs clé **étrangère** (exemple : `users.id` et `orders.user_id`).
12. **INNER JOIN** vs **LEFT JOIN**. Comment tu trouves une commande **orpheline**.
13. Pourquoi un QA ouvre SQL, pas seulement Postman / l’IHM.

## Git / GitHub

14. **Git** vs **GitHub**.
15. `add`, `commit`, `push` — à quoi sert chaque étape.

## XPath (simple)

16. C’est quoi un **XPath** ? À quoi ça sert quand tu testes une page ? (pas besoin d’écrire un XPath long)

## Agile / Scrum

17. Méthode **classique** vs **Agile** (en gros).
18. Les 4 réunions de sprint : **planning**, **daily**, **review**, **rétro** — une phrase chacune.
19. Une **User Story** arrive dans le sprint. Tu fais quoi, dans l’ordre (gros).
20. **Kick-off**, **cadrage**, **REX**, **clôture** — une phrase chacune.

---

Oral dans le chat : Q1 → tu réponds → correction → suivante.
