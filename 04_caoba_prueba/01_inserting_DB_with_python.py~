import sys,os
import functions
import csv
import psycopg2
#conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
#cur = conn.cursor()
#c
#with open(file_name, 'r') as f:
#reader = csv.reader(f,delimiter=";")
#next(reader) # Skip the header row.
#for row in reader:
#cur.execute(
#"INSERT INTO users VALUES (%s, %s, %s, %s)",
#row
#)
#conn.commit()

def pg_load_table(file_path, table_name, dbname, host, user,pwd):
    '''
    This function upload csv to a target table
    '''
    try:
        conn = psycopg2.connect(dbname=dbname, host=host,user=user,password=pwd)
        print("Connecting to Database")
        cur = conn.cursor()
        f = open(file_path, "r")
        # Truncate the table first
        cur.execute("Truncate {} Cascade;".format(table_name))
        print("Truncated {}".format(table_name))
        # Load table from the file with header
        cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
        cur.execute("commit;")
        print("Loaded data into {}".format(table_name))
        conn.close()
        print("DB connection closed.")

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

# Execution Example
file_path = functions.getting_path()
table_name = 'renata.db'
dbname = 'postgres'
host = 'localhost'
#port = '5432'
user = 'postgres'
pwd = '1234'
pg_load_table(file_path, table_name, dbname, host, user,pwd)


