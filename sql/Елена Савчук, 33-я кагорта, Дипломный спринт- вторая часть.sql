-- 1. Запрос № 1
SELECT "Couriers".login, COUNT(*) FROM "Couriers" INNER JOIN "Orders" ON "Couriers".id = "Orders"."courierId" WHERE "Orders"."inDelivery" = True GROUP BY "Couriers".login;


-- 2. Запрос № 2
SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END AS status FROM "Orders";

