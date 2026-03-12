from extract import extract_data
from transform import transform_data
from load import load_data


def run_etl():
    print("\n🚀 ETL Pipeline Started...")
    print("=" * 40)

    # Extract
    print("\n📤 Step 1: Extracting Data...")
    df = extract_data()

    # Transform
    print("\n⚙️  Step 2: Transforming Data...")
    df = transform_data(df)

    # Load
    print("\n📥 Step 3: Loading Data...")
    load_data(df)

    print("\n" + "=" * 40)
    print("✅ ETL Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_etl()