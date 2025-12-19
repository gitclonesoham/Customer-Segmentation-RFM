WITH rfm AS (
    SELECT
        customer_id,
        CURRENT_DATE - MAX(order_date) AS recency,
        COUNT(DISTINCT order_id) AS frequency,
        SUM(sales) AS monetary
    FROM sales
    GROUP BY customer_id
),
scores AS (
    SELECT
        customer_id,
        NTILE(4) OVER (ORDER BY recency DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency) AS f_score,
        NTILE(4) OVER (ORDER BY monetary) AS m_score
    FROM rfm
)
SELECT
    customer_id,
    r_score,
    f_score,
    m_score,
    (r_score + f_score + m_score) AS rfm_score,
    CASE
        WHEN (r_score + f_score + m_score) >= 10 THEN 'High Value'
        WHEN (r_score + f_score + m_score) BETWEEN 7 AND 9 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_segment
FROM scores
ORDER BY rfm_score DESC;
