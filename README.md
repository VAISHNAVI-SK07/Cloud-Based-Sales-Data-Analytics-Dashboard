# Cloud-Based-Sales-Data-Analytics-Dashboard


🚀 Cloud-Native Sales Data Pipeline & Analytics
AWS | Python | Power BI

📌 Project Overview
I developed an end-to-end data engineering pipeline to solve a common business challenge: Automating the journey from raw cloud storage to executive-level insights. This project handles the extraction, transformation, and visualization of global sales data ($1.13M+ in revenue) using a modern cloud-first approach.

🏗️ Technical Architecture
Data Source: Raw sales data stored in Amazon S3 (Mumbai Region: ap-south-1).

ETL Layer (Python): * Used Boto3 to establish a secure programmatic connection to AWS.

Leveraged Pandas for data cleaning, handling missing values, and engineering the Total Revenue metric.

Data Storage: Processed and cleaned data is uploaded back to a designated S3 bucket.

BI Layer (Power BI): Developed a dynamic dashboard featuring cross-filtering to analyze sales performance by country, product line, and order status.

📊 Business Key Performance Indicators (KPIs)
Total Revenue: $1.13 Million

Top Market: USA (Leading by volume)

High-Growth Category: Classic Cars (Highest revenue product line)

Operational Efficiency: Real-time tracking of 'Shipped' vs. 'Disputed' orders.

🛠️ How to Use This Repository
[!IMPORTANT]

To protect cloud security, AWS credentials have been replaced with placeholders in the script.

Prerequisites:

Setup:

Update the AWS_ACCESS_KEY and AWS_SECRET_KEY in etl_process.py.

Configure your S3 bucket name in the script.

Execution:

Run the Python script to sync the cloud data.

Open the .pbix file in Power BI Desktop to explore the dashboard.

📂 Repository Contents
etl_process.py - The Python logic for the cloud pipeline.

Sales_Dashboard.pbix - The final interactive dashboard (Storm Theme).

sales_data_sample.csv - Sample dataset for testing.
