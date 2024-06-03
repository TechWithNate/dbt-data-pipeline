# An ELT data pipeline Using DBT, Snowflake and Airflow
A dbt data pipeline capstone project.

<h1 align="center">ETL Data pipeline Project</h1>

<p align="center">
  <a href="#technologies">Technologies</a> •
  <a href="#about-the-project">About the project</a> •
  <a href="#conceptual-architecture">Conceptual architecture</a> •
  <a href="#conceptual-report-on-the-technologies-used">Conceptual Report on the Technologies used</a> •
  <a href="#project-setup">Project Set up</a>
</p>

---

## Technologies
 ![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)
 ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
 ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Snowflake](https://a11ybadges.com/badge?logo=snowflake)
 ![dbt](https://a11ybadges.com/badge?logo=dbt)

 ---

## About the project

A data engineering training project to build an end-to-end data pipline for a real-time processing of data. The project implements an ELT batch data processing. 
Data is fetched daily using airflow into into a snowflake data warehouse for further analysis.

In addition, process data can then be used for visual analytics.

---

## Conceptual architecture

```bash
           +-------------------------+
           |   External Data Source  |
           +-------------------------+
                      |
                      V
           +-------------------------+
           |       Snowflake         |
           |      Data Warehouse     |
           +-------------------------+
                      |
                      V
+------------------------------------------------------+
|                  ELT Pipeline (Airflow)              |
|                                                      |
|               +--------------+     +------------+    |
|               |    Extract   | --> |    Load    |    |
|               +--------------+     +------------+    |
|                        |                     |        |
|                        V                     V        |
|               +--------------+     +------------+    |
|               |   Transform  |     | dbt Models |    |
|               +--------------+     +------------+    |
+------------------------------------------------------+
```
  
---

## Conceptual Report on the Technologies used
### dbt (Data Build Tool)
Definition: dbt (data build tool) is an open-source command-line tool that enables data analysts and engineers to transform data in their warehouses more effectively. It allows users to write modular, SQL-based transformation logic in the form of "models" and run these transformations against their data warehouse.

| Pros | Cons |
| --- | --- |
| **SQL-based:** Allows analysts to write transformations using familiar SQL syntax. | **Customization:** Increased customization for incremental models to support larger data sets |
| **Modular:** Encourages the creation of modular, reusable transformation logic. | **Learning Curve:** Requires knowledge of SQL and familiarity with dbt concepts. |
| **Testing:** Provides built-in testing capabilities to ensure data quality and correctness. | **Dependency Management:** Managing dependencies between models can become complex in larger projects. |

---
### Snowflake
Snowflake is a cloud-based data warehousing platform that provides a fully managed service for storing, analyzing, and processing large volumes of data. It offers features such as elastic scaling, separation of storage and compute, and support for structured and semi-structured data.

| Pros | Cons |
| --- | --- |
| Handles infrastructure management, optimization, and tuning, allowing users to focus on data analysis. | Pricing can be higher compared to self-managed solutions, especially for large workloads. |
| Supports JSON, Avro, Parquet, and other semi-structured data formats. | Managing data pipelines and access controls can be complex in larger deployments. |
|  Allows users to scale compute independently of storage, providing cost efficiency. | Being a cloud-specific service, migrating away from Snowflake can be challenging. | 

### Airflow (Apache Airflow)
Apache Airflow is an open-source workflow orchestration tool used for scheduling, monitoring, and managing complex data pipelines. It allows users to define workflows as directed acyclic graphs (DAGs) and execute tasks in a distributed and fault-tolerant manner.
| Pros | Cons |
| --- | --- |
| Enables the creation and management of complex data pipelines as DAGs. | Setting up and configuring Airflow can be complex, especially for beginners. |
| Provides built-in monitoring and alerting capabilities to track pipeline progress and detect failures. | Requires resources for running the Airflow scheduler, web server, and worker nodes. |
| Supports dynamic DAG generation based on runtime parameters and conditions. | Users need to learn Airflow concepts such as DAGs, operators, sensors, and hooks. |

---

## Project Setup
### Step 1: Create a snowflake account and setup snowflake environment
```bash

-- create accounts
use role accountadmin;

create warehouse dbt_wh with warehouse_size='x-small';
create database if not exists dbt_db;
create role if not exists dbt_role;

show grants on warehouse dbt_wh;

grant role dbt_role to user jayzern;
grant usage on warehouse dbt_wh to role dbt_role;
grant all on database dbt_db to role dbt_role;

use role dbt_role;

create schema if not exists dbt_db.dbt_schema;

-- clean up
use role accountadmin;

drop warehouse if exists dbt_wh;
drop database if exists dbt_db;
drop role if exists dbt_role;

```
### Step 2. Clone the repository
```bash
git clone https://github.com/TechWithNate/dbt-data-pipeline
```
### Step 3. Install the requirements 
Open your terminal and run the command
```bash
pip install -r requirements.txt
```
