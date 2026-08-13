# Azure End-to-End Data Engineering Project

An end-to-end data engineering pipeline built on Microsoft Azure that ingests raw data and processes it through a **Medallion (Bronze → Silver → Gold) architecture**, landing in a **Microsoft Fabric Warehouse** — using **Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks (Spark), and Delta Live Tables**.

---

## 📌 Project Overview

This project simulates a real-world enterprise data pipeline. Raw data is pulled from multiple sources, ingested into a data lake, transformed through progressive layers of cleaning and modeling, and finally loaded into external Delta tables on Azure.

**Goals of this project:**
- Build a scalable, cloud-native ETL/ELT pipeline
- Apply the Medallion architecture pattern (Bronze / Silver / Gold)
- Practice orchestration and transformation on Azure
- Model curated data into a Star Schema

---

## 🏗️ Architecture

```
  Sources: Azure SQL Database  +  raw files
                    │
                    ▼
     Azure Data Factory (Orchestration & Ingestion)
        secured via Managed Identity + Azure Key Vault
                    │
                    ▼
   Azure Data Lake Storage Gen2 — 🥉 Bronze Layer (raw data)
                    │
                    ▼
      Azure Databricks + Spark (Transformation)
        → cleans data & models it into a Star Schema
                    │
                    ▼
   Azure Data Lake Storage Gen2 — 🥈 Silver Layer (modeled data)
                    │
                    ▼
      Azure Databricks + Delta Live Tables
        → applies business rules / aggregations
                    │
                    ▼
   Azure Data Lake Storage Gen2 — 🥇 Gold Layer (curated data)
  
```


---

## 🛠️ Tech Stack

| Category | Tools/Services |
|---|---|
| Cloud Platform | Microsoft Azure |
| Data Sources | Azure SQL Database, GitHub (raw files) |
| Orchestration | Azure Data Factory (ADF) |
| Storage | Azure Data Lake Storage Gen2 (ADLS Gen2) |
| Transformation | Azure Databricks, Apache Spark, Delta Live Tables |
| Data Modeling | Star Schema |
| Data Warehouse | Azure Data Lake Storage Gen2 (External Delta Tables) |
| Security | Azure Key Vault, Managed Identity |
| Language | Python (PySpark), SQL |
| Version Control | Git & GitHub |

---

## 📂 Data Sources

This project ingests data from **two different source types**, a common real-world pattern:

- **Azure SQL Database** — relational source data, connected via a Linked Service in ADF
- **GitHub (HTTP source)** — raw CSV/flat files pulled directly via an HTTP connector in ADF


---

## ⚙️ Pipeline Walkthrough

### 1. Ingestion (Bronze Layer)
- Provisioned **Azure Data Factory** and configured **Linked Services** to two sources:
  - **Azure SQL Database** (relational tables)
  - **GitHub** (raw files via HTTP connector)
- Secured all connections using **Managed Identity** and secrets stored in **Azure Key Vault** (no credentials hard-coded in pipelines).
- Built Copy Data pipelines to bring data from both sources into ADLS Gen2 under the `bronze/` container, preserved in its raw, unmodified form.

### 2. Transformation & Modeling (Silver Layer)
- Connected **Azure Databricks** to ADLS Gen2 using secure, identity-based access (backed by Key Vault-managed secrets).
- Used **Spark** to:
  - Clean nulls, fix data types, remove duplicates
  - Join and restructure data into a **Star Schema** (fact tables + dimension tables)
- Output written to the `silver/` container in the data lake.

### 3. Business Aggregation (Gold Layer)
- Used **Delta Live Tables** in Databricks to build a declarative, managed pipeline on top of the Silver layer.
- Applied business logic, data quality expectations, and aggregations.
- Final curated tables written to the `gold/` container as Delta tables.

---

## 🔐 Security & Access Management
- Used **Managed Identity** for secure, credential-free authentication between Azure services (ADF, Databricks, Storage).
- Stored connection strings/secrets in **Azure Key Vault** and referenced them from ADF Linked Services instead of hard-coding credentials.
- Applied **role-based access control (RBAC)** — assigned appropriate roles (e.g. `Storage Blob Data Contributor`) to ADF and Databricks identities on the storage account.

--

## 📸 Screenshots

| Stage | Screenshot |
|---|---|
| Azure Resource Group Setup |  ![Resource Group](screenshots/Azure%20-%20Resources.png) |
| ADF Pipeline (Bronze Ingestion) | ![Resource Group](screenshots/Full%20ADF%20Pipeline.png) |
| Databricks Notebook (Silver Transform) | ![Resource Group](screenshots/DBX-%20Silver%20-%20Autoloader-%20Write.png) |
| Databricks DLT (Gold Transform) | ![Resource Group](screenshots/DBX-%2520DLT%2520Pipeline%2520-%2520Holistic.png) |

---

## 📁 Repository Structure

```
├── adf/                     # ADF pipeline JSON exports / ARM templates
├── databricks-notebooks/    # Spark notebooks & Delta Live Tables pipelines for Silver & Gold
├── screenshots/             # Project screenshots
├── datasets/                # Sample/raw data (if applicable)
└── README.md
```

---

## 🚀 How to Reproduce This Project

1. **Create Azure resources:**
   - Resource Group
   - Storage Account (ADLS Gen2 enabled)
   - Azure Data Factory
   - Azure Databricks workspace
   - Microsoft Fabric workspace (Warehouse)
2. **Set up Linked Services** in ADF for the Azure SQL Database and GitHub sources, plus the ADLS Gen2 sink (secure with Key Vault + Managed Identity).
3. **Build and run the ingestion pipeline** to load raw data into the Bronze layer.
4. **Run the Databricks notebooks** (`/databricks-notebooks`) to model Bronze → Silver (Star Schema) and Silver → Gold (Delta Live Tables).
5. **load it** to the Gold layer.
---

## 🎯 Key Learnings

- Designing and implementing the **Medallion architecture** (Bronze / Silver / Gold) on Azure
- Ingesting from **multiple heterogeneous sources** (Azure SQL Database + GitHub) with Azure Data Factory
- Securing pipelines with **Azure Key Vault** and Managed Identity instead of hard-coded credentials
- Modeling data into a **Star Schema** using Spark on Azure Databricks
- Building declarative, managed pipelines with **Delta Live Tables**

---

## 👤 Author

**Mohit Pandey**



[![Gmail](https://img.shields.io/badge/Gmail-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mr.mohitreally@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/mohit-pandey-data-engineer)
