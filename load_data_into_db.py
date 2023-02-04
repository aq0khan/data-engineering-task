import read_csv
import psycopg2
df = read_csv
df = df.dropna()
def store_data(table_name):
    conn = psycopg2.connect(
            database="challenge",
            user="pipeline",
            password="pipeline-pass"
        )
    cursor = conn.cursor()
    check_table_query = f"SELECT to_regclass('public.{table_name}')"
    cursor.execute(check_table_query)
    if cursor.fetchone()[0] is not None:
        # Insert the data into the table
        for i, row in df.iterrows():
            insert_statement = "INSERT INTO {} ({}) VALUES ({})".format(
                table_name,
                ",".join(df.columns),
                ",".join(["'{}'".format(x) if type(x) == str else str(x) for x in row])
            )
            cursor.execute(insert_statement)

        # Commit the changes to the database
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()