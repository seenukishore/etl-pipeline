# 🔄 ETL Pipeline Project

## 📌 About
A Python-based ETL (Extract, Transform, Load) Pipeline that extracts raw sales data from MySQL, transforms it using Pandas, and loads it into a Data Warehouse.

## 🛠️ Technologies Used
- Python 3
- MySQL Connector
- Pandas
- SQLAlchemy
- Cryptography (Fernet)

## 📁 Project Structure
| File | Description |
|------|-------------|
| `etl_runner.py` | Main ETL pipeline runner |
| `extract.py` | Extracts data from sales_db |
| `transform.py` | Cleans and transforms data |
| `load.py` | Loads data into sales_warehouse |
| `password_utils.py` | Encrypted password handler |
| `.gitignore` | Hides secret.key from GitHub |

## ⚙️ ETL Process
- 📤 **Extract** → Raw data from `sales_db.raw_sales`
- ⚙️ **Transform** → Remove duplicates, calculate `total_amount`, title case names
- 📥 **Load** → Clean data into `sales_warehouse.fact_sales`

## 🔒 Security
- `secret.key` is never uploaded to GitHub
- Password is encrypted using Fernet encryption

## ▶️ How to Run
1. Clone the repository
2. Install dependencies:
```
   pip install mysql-connector-python pandas sqlalchemy cryptography
```
3. Setup MySQL databases `sales_db` and `sales_warehouse`
4. Run `etl_runner.py`