import pandas as pd


def transform_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Remove null values
    df = df.dropna()

    # Calculate total amount
    df['total_amount'] = df['quantity'] * df['price']

    # Rename price column
    df = df.rename(columns={'price': 'unit_price'})

    # Capitalize customer names
    df['customer_name'] = df['customer_name'].str.title()

    # Capitalize region
    df['region'] = df['region'].str.title()

    print(f"✅ Transformed {len(df)} records successfully")
    return df