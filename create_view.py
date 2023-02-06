import psycopg2

conn = psycopg2.connect('postgresql://') #connnection string
cursor = conn.cursor()
table_name = 'customer_data'
check_view_query = """
SELECT * 
FROM information_schema.views 
WHERE table_name = 'customer_data';
"""

cursor.execute(check_view_query)
view_exists = cursor.fetchone()

if not view_exists:
    create_view_query = """
    CREATE VIEW data_view AS
    SELECT 
      customer_name, 
      order_id, 
      product_name, 
      SUM(quantity) AS total_quantity, 
      SUM(product_cost) AS total_cost 
    FROM 
      customer_data 
    GROUP BY 
      customer_name, 
      order_id, 
      product_name;
    """

    cursor.execute(create_view_query)
    conn.commit()
cursor.close()
conn.close()
