import psycopg2

conn = psycopg2.connect('') #connection string
cursor = conn.cursor()

select_view_query = """
SELECT * 
FROM data_view;
"""

cursor.execute(select_view_query)
headers = [header[0] for header in cursor.description]
view_data = cursor.fetchall()

print(headers)

for row in view_data:
    print(row)

cursor.close()
conn.close()
