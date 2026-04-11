import argparse
from db import get_connection
import queries

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--report",
        help="report name to fetch",
        type=str,
        required=True
    )
    args = parser.parse_args()

    get_report(args.report)

def get_report(report_name):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    if report_name == "sales_summary":
        cursor.execute(queries.total_sales())
        sales = cursor.fetchone()[0]

        cursor.execute(queries.total_orders())
        orders = cursor.fetchone()[0]

        print(f"Orders placed = {orders}, Total Sales = {sales}")

    elif report_name == "top_product":
        cursor.execute(queries.top_product())
        result = cursor.fetchone()
        print(f"Top Product: {result[0]} ({result[1]})")



if __name__ == "__main__":
    main()