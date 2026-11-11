-- Contrôles QA sur qa_training.db (users, orders, order_items, products)

-- Commandes avec email du client
SELECT o.id, o.total_amount, u.email
FROM orders o
INNER JOIN users u ON o.user_id = u.id;

-- Commandes sans client (orphelin)
SELECT o.id, o.user_id, o.total_amount
FROM orders o
LEFT JOIN users u ON o.user_id = u.id
WHERE u.id IS NULL;

-- Lignes panier sans commande
SELECT oi.id, oi.order_id
FROM order_items oi
LEFT JOIN orders o ON oi.order_id = o.id
WHERE o.id IS NULL;

-- Lignes panier avec nom du produit
SELECT oi.id, oi.order_id, p.name
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id;

-- Ventes d’un produit retiré
SELECT oi.id, p.name, p.is_active
FROM order_items oi
INNER JOIN products p ON oi.product_id = p.id
WHERE p.is_active = 0;

-- Commandes dont le total ≠ somme des lignes
SELECT o.id, o.total_amount, SUM(oi.quantity * oi.unit_price) AS prix_lignes
FROM orders o
INNER JOIN order_items oi ON oi.order_id = o.id
GROUP BY o.id, o.total_amount
HAVING o.total_amount != SUM(oi.quantity * oi.unit_price);

-- Commandes d’un user inactive
SELECT o.id, u.status, u.email
FROM orders o
INNER JOIN users u ON u.id = o.user_id
WHERE u.status = 'inactive';

-- Ligne panier + email + nom produit (commande et client connus)
SELECT oi.id, oi.order_id, u.email, p.name
FROM users u
INNER JOIN orders o ON u.id = o.user_id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id;

-- Users sans commande
SELECT u.id, u.email
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE o.id IS NULL;

-- Nombre de commandes par user (au moins une)
SELECT u.id, u.email, COUNT(*) AS nb_commandes
FROM users u
INNER JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.email;

-- Commandes au-dessus de la moyenne
SELECT id, total_amount
FROM orders
WHERE total_amount > (SELECT AVG(total_amount) FROM orders);

-- Commandes en dessous de la moyenne
SELECT id, total_amount
FROM orders
WHERE total_amount < (SELECT AVG(total_amount) FROM orders);
