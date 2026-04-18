def total_sales():
    return "Select SUM(amount) from sales"

def total_sales_filtered():
    return "Select SUM(amount) FROM sales WHERE sale_date BETWEEN %s AND %s"

def total_orders():
    return "Select COUNT(*) from sales"

def total_orders_filtered():
    return "Select COUNT(*) from sales WHERE sale_date BETWEEN %s AND %s"

def top_products():
    return """
    SELECT product, SUM(amount) AS total
    FROM sales
    GROUP BY product
    ORDER BY total DESC
    LIMIT %s
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

def monthly_sales():
    return """
    SELECT DATE_FORMAT(sale_date, '%Y-%m') AS month,
           SUM(amount) AS total
    FROM sales
    GROUP BY month
    ORDER BY month;
    """