import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://<YOUR_USERNAME>@localhost:5432/sales_analysis",
    connect_args={"password": "<YOUR_PASSWORD>"}
)


# Customer segment count

segment_query = """
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
    CASE
        WHEN (r_score + f_score + m_score) >= 10 THEN 'High Value'
        WHEN (r_score + f_score + m_score) BETWEEN 7 AND 9 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS segment
FROM scores;
"""

df_segments = pd.read_sql(segment_query, engine)

df_segments['segment'].value_counts().plot(kind='bar')
plt.title("Customer Count by Segment")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.show()


# Revenue by segment

revenue_query = """
WITH customer_metrics AS (
    SELECT
        customer_id,
        COUNT(order_id) AS frequency,
        SUM(sales) AS monetary,
        CURRENT_DATE - MAX(order_date) AS recency
    FROM sales
    GROUP BY customer_id
),
rfm_scores AS (
    SELECT
        customer_id,
        monetary,
        NTILE(4) OVER (ORDER BY recency DESC) AS r_score,
        NTILE(4) OVER (ORDER BY frequency) AS f_score,
        NTILE(4) OVER (ORDER BY monetary) AS m_score
    FROM customer_metrics
)
SELECT
    CASE
        WHEN (r_score + f_score + m_score) >= 10 THEN 'High Value'
        WHEN (r_score + f_score + m_score) BETWEEN 7 AND 9 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS segment,
    ROUND(SUM(monetary), 2) AS total_revenue
FROM rfm_scores
GROUP BY segment;

"""

df_revenue = pd.read_sql(revenue_query, engine)

df_revenue.plot(kind='bar', x='segment', y='total_revenue', legend=False)
plt.title("Revenue Contribution by Segment")
plt.xlabel("Segment")
plt.ylabel("Total Revenue")
plt.show()


# Recency vs Frequency

rf_query = """
SELECT
    customer_id,
    CURRENT_DATE - MAX(order_date) AS recency,
    COUNT(order_id) AS frequency
FROM sales
GROUP BY customer_id;
"""

rf_df = pd.read_sql(rf_query, engine)

plt.scatter(rf_df["recency"], rf_df["frequency"], alpha=0.5)
plt.title("Recency vs Frequency")
plt.xlabel("Recency (days)")
plt.ylabel("Frequency")
plt.show()
 

