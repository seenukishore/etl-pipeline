import mysql.connector
from password_utils import get_decrypted_password

def load_data(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="sales_warehouse"
    )
    cursor = conn.cursor()

    # Clear old data
    cursor.execute("DELETE FROM fact_sales")

    # Insert transformed data
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO fact_sales 
            (customer_name, product, quantity, unit_price, total_amount, sale_date, region)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['customer_name'],
            row['product'],
            row['quantity'],
            row['unit_price'],
            row['total_amount'],
            row['sale_date'],
            row['region']
        ))

    conn.commit()
    conn.close()
    print(f"✅ Loaded {len(df)} records into sales_warehouse")