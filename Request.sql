Логин курьера и число заказов в доставке

SELECT c.login,
       COUNT(o.id) AS orders_in_delivery
FROM "Couriers" AS c
JOIN "Orders" AS o ON o."courierId" = c.id
WHERE o."inDelivery" = TRUE
GROUP BY c.login;

Трекер заказов и статус 

SELECT track,
       CASE
           WHEN finished = TRUE THEN 2
           WHEN cancelled = TRUE THEN -1
           WHEN "inDelivery" = TRUE THEN 1
           ELSE 0
       END AS status
FROM "Orders";