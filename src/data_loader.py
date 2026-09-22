import pandas as pd
from pathlib import Path


def load_raw_data(data_dir: Path) -> dict:
    """Load the Northwind raw datasets."""

    tables = {
        "orders": "Orders.csv",
        "order_details": "Order Details.csv",
        "products": "Products.csv",
        "customers": "Customers.csv",
        "employees": "Employees.csv",
    }

    data = {}

    for table_name, filename in tables.items():
        filepath = data_dir / filename

        if not filepath.exists():
            raise FileNotFoundError(f"File not found: {filepath}")

        data[table_name] = pd.read_csv(filepath)

    return data
