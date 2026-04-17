import argparse
from db import get_connection
import queries
from logger import get_logger
import csv

logger = get_logger()
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--report",
        help="report name to fetch",
        type=str,
        required=True
    )

    parser.add_argument(
        "--start_date",
        help="start date of the report",
        type=str,
    )

    parser.add_argument(
        "--end_date",
        help="end date of the report",
        type=str,
    )

    parser.add_argument(
        "--export",
        help="csv file name to export report to",
        type=str,
    )

    args = parser.parse_args()

    get_report(args)

def export_to_csv(filename, headers, data):
    
    with open(filename, "w", newline="", encoding='utf-8') as f:

        if isinstance(data, list) and all(isinstance(x, tuple) for x in data):
            writer = csv.writer(f)
            writer.writerow(headers)

            for row in data:
                writer.writerow(row)

        elif isinstance(data, list):
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow(data)

def get_report(args):
    db_conn = get_connection()
    cursor = db_conn.cursor()

    if args.report == "sales_summary":
        try:
            if args.start_date and args.end_date:
                cursor.execute(queries.total_sales_filtered(),(args.start_date,args.end_date))
                sales = cursor.fetchone()[0]
                
                cursor.execute(queries.total_orders_filtered(),(args.start_date,args.end_date))
                orders = cursor.fetchone()[0]

            else:
                cursor.execute(queries.total_sales())
                sales = cursor.fetchone()[0]

                cursor.execute(queries.total_orders())
                orders = cursor.fetchone()[0]
            logger.info(f"Orders placed = {orders}, Total Sales = {sales}")
            if args.export:
                export_to_csv(args.export,["Total Orders", "Total Sales"], [orders, sales])

        except Exception as e:
            logger.error(f"Error: {e}")
    

    elif args.report == "sales_by_customer":

        try:
            cursor.execute(queries.sales_by_customer())
            results = cursor.fetchall()

            for row in results:
                logger.info(f"{row[0]}->{row[1]}")
            
            if args.export:
                export_to_csv(args.export,["Name", "Total Sales"], results)
        
        except Exception as e:
            logger.error(f"Error: {e}")

    elif args.report == "top_product":

        cursor.execute(queries.top_product())
        result = cursor.fetchone()
        logger.info(f"Top Product: {result[0]} ({result[1]})")


if __name__ == "__main__":
    main()