import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from password_utils import get_decrypted_password


def extract_data():
    password = quote_plus(str.__str__(get_decrypted_password()))
    engine = create_engine(f"mysql+mysqlconnector://root:{password}@localhost/sales_db")

    query = "SELECT * FROM raw_sales"
    df = pd.read_sql(query, engine)

    print(f"✅ Extracted {len(df)} records from sales_db")
    return df