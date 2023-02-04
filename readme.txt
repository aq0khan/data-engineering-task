There are three 4 files in this project
1- read_csv : reads data from S3.
2- create_table : Create table and define schema.
3- load_data_into_db : Store data in postgres database.
3- create_view : creates view of given query in database.
5- visualize_view : print view from database.
6- To run this project you need to run runner.py only.
7- pipeline_dag : It contains airflow dag, currently showing only dag to read csv
but it's not running right now we can use airflow for track the pipeline's progress, status, and error messages.

