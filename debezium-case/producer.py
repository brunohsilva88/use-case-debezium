# IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
from sqlalchemy import create_engine
import pandas as pd
import os
import time
 
# DEFINE THE DATABASE CREDENTIALS
user = 'admin'
password = 'admin'
host = 'postgres'
port = 5432
database = 'dvdrental'

# PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# RETURN THE SQLACHEMY ENGINE OBJECT
def get_connection():
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(user, password, host, port, database), pool_pre_ping=True
    )
if __name__ == '__main__':
    try:
        engine = get_connection()
        print(f"Connection to the {host} for user {user} created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

df = pd.read_sql('Select * from public.payment', engine)
df = df[['payment_id', 'customer_id', 'staff_id', 'rental_id', 'amount', 'payment_date']]
df.head()

for index, row in df.head(150).iterrows():
    mod = pd.DataFrame(row.to_frame().T)
    mod.to_sql(f"payment_streaming", engine, if_exists='append', index=False)
    print("Row Inserted " + mod.payment_id.astype(str) + ' ' + mod.amount.astype(str).astype(str))
    time.sleep(3)