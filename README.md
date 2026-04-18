# SQL Reporting Dashboard (Python + MySQL)

## 📌 Overview

A command-line based reporting tool built using Python and MySQL to generate dynamic business insights from relational data. The application demonstrates real-world backend concepts such as database integration, SQL query design, data aggregation, and reporting.

This project was developed as a hands-on exercise to strengthen Python and SQL skills, focusing on practical data processing and reporting workflows.

---

## 🚀 Features

* 📊 Sales Summary Report (Total Sales & Orders)
* 🏆 Top-N Products (Dynamic input via CLI)
* 📅 Monthly Sales Trends
* 👥 Sales by Customer (JOIN operations)
* 🔍 Date Range Filtering
* 📁 CSV Export for reports
* 📝 Structured Logging
* ⚙️ Modular and extensible architecture

---

## 🛠️ Tech Stack

* **Language:** Python
* **Database:** MySQL
* **Libraries:**

  * argparse (CLI handling)
  * mysql-connector-python (DB connection)
  * csv (export functionality)
  * logging (application logs)

---

## 📂 Project Structure

```
sql-dashboard/
│
├── dashboard.py        # Main CLI entry point
├── db.py               # Database connection
├── queries.py          # SQL queries
├── config.py           # Configuration (DB, constants)
├── logger.py           # Logging setup
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```
git clone <your-repo-url>
cd sql-dashboard
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Setup MySQL Database

Create database:

```sql
CREATE DATABASE sales_dashboard;
USE sales_dashboard;
```

Create table:

```sql
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(100),
    amount DECIMAL(10,2),
    sale_date DATE,
    customer_id INT
);
```

Create customers table:

```sql
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
```

---

### 4. Configure Database

Update `config.py`:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "sales_dashboard"
}
```

---

## ▶️ Usage

### Run Help

```
python dashboard.py --help
```

---

### 1. Sales Summary

```
python dashboard.py --report sales_summary
```

---

### 2. Top Products

```
python dashboard.py --report top_products --top-n 3
```

---

### 3. Monthly Sales

```
python dashboard.py --report monthly_sales
```

---

### 4. Sales by Customer

```
python dashboard.py --report sales_by_customer
```

---

### 5. With Date Filter

```
python dashboard.py --report sales_summary --start-date 2024-01-01 --end-date 2024-01-05
```

---

### 6. Export to CSV

```
python dashboard.py --report top_products --top-n 3 --export report.csv
```

---

## 🧠 Key Concepts Demonstrated

* SQL Aggregations (`SUM`, `COUNT`)
* JOIN operations
* Date-based filtering
* Dynamic query handling
* CLI-based application design
* Modular architecture
* Logging and error handling

---

## 🚀 Future Improvements

* Convert CLI tool to REST API (FastAPI/Flask)
* Add visualization layer (charts/dashboard)
* Introduce connection pooling
* Add unit testing

---

## 👨‍💻 Author

Maninder Singh
(Independent Project for Python & SQL upskilling)

---
