This project reads csv files from a S3 location and then store them to postges.
There are 7 files in this project
1- read_csv.py : reads data from S3.
2- create_table.py : Create table and define schema.
3- load_data_into_db.py : Store data in postgres database.
3- create_view.py : creates view of given query in database.
5- visualize_view.py : print view from database.
6- runner.py : To run this project you need to run this file.
7- pipeline_dag.py : It contains airflow dag, currently showing only dag to read csv
but it's not running right now we can use airflow for track the pipeline's progress, status, and error messages.
