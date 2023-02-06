import psycopg2
def ddl(table_name):
    conn = psycopg2.connect(
        database="", 
        user="",
        password=""
    ) #connection string
    cursor = conn.cursor()
    check_table_query = f"SELECT to_regclass('public.{table_name}')"
    cursor.execute(check_table_query)
    if cursor.fetchone()[0] is None:
        new_table = f""" CREATE TABLE {table_name} (
                                    order_id SERIAL PRIMARY KEY,
                                    customer_name VARCHAR,
                                    product_name VARCHAR,
                                    quantity int,
                                    order_date Date,
                                    location VARCHAR,
                                    email VARCHAR,
                                    phone VARCHAR,
                                    product_cost FLOAT
                            );
    """
        cursor.execute(new_table)
        conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()
ddl("test")
