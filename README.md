# Azure End-to-End Data Engineering Project

An end-to-end data engineering pipeline built on Microsoft Azure that ingests raw data and processes it through a **Medallion (Bronze → Silver → Gold) architecture**, landing in a **Microsoft Fabric Warehouse** — using **Azure Data Factory, Azure Data Lake Storage Gen2, Azure Databricks (Spark), and Delta Live Tables**.

---

## 📌 Project Overview

This project simulates a real-world enterprise data pipeline. Raw data is pulled from multiple sources, ingested into a data lake, transformed through progressive layers of cleaning and modeling, and finally loaded into a warehouse for analytics.

**Goals of this project:**
- Build a scalable, cloud-native ETL/ELT pipeline
- Apply the Medallion architecture pattern (Bronze / Silver / Gold)
- Practice orchestration and transformation on Azure
- Model curated data into a Star Schema and serve it via a Fabric Warehouse

---

## 🏗️ Architecture


<svg width="680" height="920" viewBox="0 0 680 920" xmlns="http://www.w3.org/2000/svg" role="img">
<title>Azure data engineering pipeline architecture</title>
<desc>Data flows from Azure SQL Database and GitHub, through Azure Data Factory into a Bronze layer, is modeled into a star schema via Azure Databricks and Spark into a Silver layer, refined with Delta Live Tables into a Gold layer, and finally served through Microsoft Fabric as a data warehouse.</desc>
<defs>
<marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
<path d="M2 1L8 5L2 9" fill="none" stroke="#73726c" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
</marker>
</defs>
<rect x="0" y="0" width="680" height="920" fill="#FFFFFF"/>

<!-- Connectors -->
<line x1="340" y1="96" x2="340" y2="152" stroke="#73726c" stroke-width="1" marker-end="url(#arrow)"/>
<line x1="340" y1="208" x2="340" y2="264" stroke="#73726c" stroke-width="1" marker-end="url(#arrow)"/>
<line x1="340" y1="320" x2="340" y2="376" stroke="#73726c" stroke-width="1" marker-end="url(#arrow)"/>
<line x1="340" y1="432" x2="340" y2="488" stroke="#73726c" stroke-width="1" marker-end="url(#arrow)"/>
<line x1="340" y1="544" x2="340" y2="600" stroke="#73726c" stroke-width="1" marker-end="url(#arrow)"/>
<line x1="340" y1="656" x2="340" y2="712" stroke="#73726c" stroke-width="1" marker-end="url(#arrow)"/>
<line x1="340" y1="768" x2="340" y2="824" stroke="#73726c" stroke-width="1" marker-end="url(#arrow)"/>

<!-- Security badge -->
<rect x="390" y="98" width="230" height="28" rx="14" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
<text x="505" y="112" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#085041" text-anchor="middle" dominant-baseline="central">Key Vault &amp; managed identity</text>

<!-- Box 1: Data sources -->
<rect x="60" y="40" width="560" height="56" rx="8" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
<text x="340" y="64" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#444441" text-anchor="middle" dominant-baseline="central">Data sources</text>
<text x="340" y="82" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">Azure SQL Database + GitHub</text>

<!-- Box 2: Azure Data Factory -->
<rect x="60" y="152" width="560" height="56" rx="8" fill="#E6F1FB" stroke="#185FA5" stroke-width="0.5"/>
<text x="340" y="176" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#0C447C" text-anchor="middle" dominant-baseline="central">Azure Data Factory</text>
<text x="340" y="194" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#185FA5" text-anchor="middle" dominant-baseline="central">Secure, orchestrated ingestion</text>

<!-- Box 3: Bronze layer -->
<rect x="60" y="264" width="560" height="56" rx="8" fill="#FAECE7" stroke="#993C1D" stroke-width="0.5"/>
<text x="340" y="288" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#712B13" text-anchor="middle" dominant-baseline="central">Bronze layer</text>
<text x="340" y="306" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#993C1D" text-anchor="middle" dominant-baseline="central">Raw data landing zone</text>

<!-- Box 4: Azure Databricks + Spark -->
<rect x="60" y="376" width="560" height="56" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
<text x="340" y="400" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#085041" text-anchor="middle" dominant-baseline="central">Azure Databricks + Spark</text>
<text x="340" y="418" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#0F6E56" text-anchor="middle" dominant-baseline="central">Star schema modeling</text>

<!-- Box 5: Silver layer -->
<rect x="60" y="488" width="560" height="56" rx="8" fill="#F1EFE8" stroke="#5F5E5A" stroke-width="0.5"/>
<text x="340" y="512" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#444441" text-anchor="middle" dominant-baseline="central">Silver layer</text>
<text x="340" y="530" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#5F5E5A" text-anchor="middle" dominant-baseline="central">Cleaned, modeled data</text>

<!-- Box 6: Delta Live Tables -->
<rect x="60" y="600" width="560" height="56" rx="8" fill="#E1F5EE" stroke="#0F6E56" stroke-width="0.5"/>
<text x="340" y="624" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#085041" text-anchor="middle" dominant-baseline="central">Delta Live Tables</text>
<text x="340" y="642" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#0F6E56" text-anchor="middle" dominant-baseline="central">Declarative data pipelines</text>

<!-- Box 7: Gold layer -->
<rect x="60" y="712" width="560" height="56" rx="8" fill="#FAEEDA" stroke="#854F0B" stroke-width="0.5"/>
<text x="340" y="736" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#633806" text-anchor="middle" dominant-baseline="central">Gold layer</text>
<text x="340" y="754" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#854F0B" text-anchor="middle" dominant-baseline="central">Curated, aggregated data</text>

<!-- Box 8: Microsoft Fabric -->
<rect x="60" y="824" width="560" height="56" rx="8" fill="#EEEDFE" stroke="#534AB7" stroke-width="0.5"/>
<text x="340" y="848" font-family="Helvetica, Arial, sans-serif" font-size="14" font-weight="600" fill="#3C3489" text-anchor="middle" dominant-baseline="central">Microsoft Fabric</text>
<text x="340" y="866" font-family="Helvetica, Arial, sans-serif" font-size="12" fill="#534AB7" text-anchor="middle" dominant-baseline="central">Serving data warehouse</text>

</svg>

```
 

## 🛠️ Tech Stack

| Category | Tools/Services |
|---|---|
| Cloud Platform | Microsoft Azure |
| Data Sources | Azure SQL Database, GitHub (raw files) |
| Orchestration | Azure Data Factory (ADF) |
| Storage | Azure Data Lake Storage Gen2 (ADLS Gen2) |
| Transformation | Azure Databricks, Apache Spark, Delta Live Tables |
| Data Modeling | Star Schema |
| Data Warehouse | Microsoft Fabric (Warehouse) |
| Security | Azure Key Vault, Managed Identity |
| Language | Python (PySpark), SQL |
| Version Control | Git & GitHub |

---

## 📂 Data Sources

This project ingests data from **two different source types**, a common real-world pattern:

- **Azure SQL Database** — relational source data, connected via a Linked Service in ADF
- **GitHub (HTTP source)** — raw CSV/flat files pulled directly via an HTTP connector in ADF

*(Update with the exact dataset/tables you used)*

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

### 4. Serving Layer
- Loaded/exposed the Gold layer to a **Microsoft Fabric Warehouse**, which serves as the final analytics-ready warehouse layer.

---

## 🔐 Security & Access Management
- Used **Managed Identity** for secure, credential-free authentication between Azure services (ADF, Databricks, Fabric, Storage).
- Stored connection strings/secrets in **Azure Key Vault** and referenced them from ADF Linked Services instead of hard-coding credentials.
- Applied **role-based access control (RBAC)** — assigned appropriate roles (e.g. `Storage Blob Data Contributor`) to ADF and Databricks identities on the storage account.

---

## 📸 Screenshots

> Add your own screenshots here to showcase each stage of the pipeline.

| Stage | Screenshot |
|---|---|
| Azure Resource Group Setup | `screenshots/resource-group.png` |
| ADF Pipeline (Bronze Ingestion) | `screenshots/adf-pipeline.png` |
| Databricks Notebook (Silver Transform) | `screenshots/databricks-silver.png` |
| Databricks Notebook (Gold Transform) | `screenshots/databricks-gold.png` |
| Fabric Warehouse | `screenshots/fabric-warehouse.png` |

---

## 📁 Repository Structure

```
├── adf/                     # ADF pipeline JSON exports / ARM templates
├── databricks-notebooks/    # Spark notebooks & Delta Live Tables pipelines for Silver & Gold
├── fabric/                  # Fabric Warehouse setup / SQL scripts
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
5. **Create a Warehouse in Microsoft Fabric** and load/point it to the Gold layer.

---

## 🎯 Key Learnings

- Designing and implementing the **Medallion architecture** (Bronze / Silver / Gold) on Azure
- Ingesting from **multiple heterogeneous sources** (Azure SQL Database + GitHub) with Azure Data Factory
- Securing pipelines with **Azure Key Vault** and Managed Identity instead of hard-coded credentials
- Modeling data into a **Star Schema** using Spark on Azure Databricks
- Building declarative, managed pipelines with **Delta Live Tables**
- Serving curated data through **Microsoft Fabric** as a warehouse layer

---

## 👤 Author

**[Your Name]**
📧 [your.email@example.com]
🔗 [LinkedIn](https://linkedin.com/in/yourprofile) | [Portfolio](https://yourportfolio.com)
