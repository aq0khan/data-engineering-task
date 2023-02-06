import read_csv
import create_table
import create_view
import visualize_view
import load_data_into_db
read_csv.read_csv_from_s3('', '') #bucket and folder name
create_table.ddl('customer_table') #passing table name
load_data_into_db.store_data('customer_table') #passing table name
create_view
visualize_view
