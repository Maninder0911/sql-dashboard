def total_sales():
    return "Select SUM(amount) from sales"

def total_sales_filtered():
    return "Select SUM(amount) FROM sales WHERE sale_date BETWEEN %s AND %s"

def total_orders():
    return "Select COUNT(*) from sales"

def total_orders_filtered():
    return "Select COUNT(*) from sales WHERE sale_date BETWEEN %s AND %s"

def top_product():
    return """
    SELECT product, SUM(amount) AS total
    FROM sales
    GROUP BY product
    ORDER BY total DESC
    LIMIT 1
    """

def sales_by_customer():
    return """
    SELECT c.name, SUM(amount) AS total
    FROM sales AS s
    INNER JOIN customers AS c
    ON s.customer_id = c.id
    GROUP BY c.name
    ORDER BY total DESC
    """