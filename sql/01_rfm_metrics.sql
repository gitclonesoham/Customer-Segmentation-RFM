SELECT
    customer_id,
    CURRENT_DATE - MAX(order_date) AS recency,
    COUNT(DISTINCT order_id) AS frequency,
    ROUND(SUM(sales), 2) AS monetary
FROM sales
GROUP BY customer_id;
