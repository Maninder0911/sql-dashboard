def total_sales():
    return "Select SUM(amount) from sales"

def total_orders():
    return "Select COUNT(*) from sales"

def top_product():
    return """
    SELECT product, SUM(amount) AS total
    FROM sales
    GROUP BY product
    ORDER BY total DESC
    LIMIT 1
    """