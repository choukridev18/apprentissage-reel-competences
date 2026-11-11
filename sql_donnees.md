# Données `qa_training.db`

Ouvre ce fichier. Tu compares les colonnes à l’œil.

Lien : `users.id` ← `orders.user_id` ← `order_items.order_id`  
Lien : `products.id` ← `order_items.product_id`

---

## users

| id | email | status | created_at |
|----|-------|--------|------------|
| 1 | alice@example.com | active | 2024-01-10 |
| 2 | bob@example.com | active | 2024-02-01 |
| 3 | alice@example.com | active | 2024-03-15 |
| 4 | invalid-email | active | 2024-04-01 |
| 5 | inactive@example.com | inactive | 2024-05-01 |
| 6 | *(vide)* | active | 2024-06-01 |

## products

| id | sku | name | is_active |
|----|-----|------|-----------|
| 1 | SKU-001 | Clavier | 1 |
| 2 | SKU-002 | Souris | 1 |
| 3 | SKU-OLD | Produit retiré | 0 |

## orders

| id | user_id | status | total_amount | created_at |
|----|---------|--------|--------------|------------|
| 101 | 1 | paid | 120.0 | 2024-06-01 |
| 102 | 1 | paid | 50.0 | 2024-06-02 |
| 103 | 999 | paid | 30.0 | 2024-06-03 |
| 104 | 2 | cancelled | 0.0 | 2024-06-04 |
| 105 | 2 | paid | -10.0 | 2024-06-05 |
| 106 | 5 | pending | 80.0 | 2024-06-06 |

## order_items

| id | order_id | product_id | quantity | unit_price |
|----|----------|------------|----------|------------|
| 1 | 101 | 1 | 1 | 100.0 |
| 2 | 101 | 2 | 1 | 20.0 |
| 3 | 102 | 2 | 2 | 25.0 |
| 4 | 105 | 1 | 1 | 5.0 |
| 5 | 106 | 3 | 1 | 80.0 |
| 6 | 999 | 1 | 1 | 10.0 |

---

## Exo 3 — quoi regarder

Dans `order_items`, la colonne `order_id` : **101, 101, 102, 105, 106, 999**.

Dans `orders`, la colonne `id` : **101, 102, 103, 104, 105, 106**.

**999** n’est pas dans `orders`. La ligne **6** pointe vers une commande qui n’existe pas.

`o.id` après le collage = la commande **trouvée**. Il n’y en a pas → case **vide**.  
Le **999** n’est pas dans `orders`. Il est dans `order_items.order_id` → colonne **`oi.order_id`**.
