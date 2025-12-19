# Customer Segmentation using RFM Analysis

This project focuses on segmenting customers based on their purchasing behavior using **RFM analysis (Recency, Frequency, Monetary value)**.  
The goal is to understand different customer groups and identify high-value customers using SQL and Python.

This project simulates a real-world data analytics task where transactional sales data is analyzed and converted into meaningful business insights.

---

## Dataset

The dataset used in this project is a retail sales dataset sourced from Kaggle:

**Sales Forecasting Dataset (Kaggle)**  
https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting

The dataset contains order-level information such as:
- Order dates  
- Customer details  
- Product categories  
- Sales values  

It is suitable for customer behavior analysis and business analytics use cases.

---

## Tools & Technologies

- **PostgreSQL** – Data storage and SQL analysis  
- **SQL** – Aggregations, window functions, and customer scoring  
- **Python** – Data analysis and visualization  
  - Pandas  
  - Matplotlib  

---

## Project Workflow

1. Loaded cleaned sales data into PostgreSQL  
2. Calculated RFM metrics (Recency, Frequency, Monetary value) using SQL  
3. Applied SQL window functions to score customers  
4. Segmented customers into High, Medium, and Low value groups  
5. Visualized customer segments and behavior using Python  

---

## Customer Segments

Customers were grouped into three segments:
- **High Value** – Recent, frequent, and high-spending customers  
- **Medium Value** – Moderately engaged customers  
- **Low Value** – Infrequent and low-spending customers  

---

## Visualizations

The following visualizations were created as part of the analysis:
- Customer count by segment  
- Revenue contribution by customer segment  
- Recency vs Frequency scatter plot  

These visualizations help in understanding customer behavior and business impact.

---

## Key Insights

- High-value customers contribute a significant portion of total revenue  
- A large number of customers fall into the low-value segment, indicating potential re-engagement opportunities  
- Clear behavioral differences are visible across customer segments  

---

## Conclusion

This project demonstrates an end-to-end customer segmentation workflow using SQL and Python.  
It highlights how transactional data can be transformed into actionable insights that support data-driven decision making.

 
