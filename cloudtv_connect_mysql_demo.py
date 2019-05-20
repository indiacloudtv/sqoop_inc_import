import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

print("Started ... {0}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
table_name = "transaction_detail_tbl"

host_name = "localhost"
port_no = str(3306)
user_name = "root"
password = "root"
database_name = "ecommerce_db"
mysql_jdbc_url = "mysql+mysqlconnector://" + user_name + ":" + password + "@" + host_name + ":" + port_no + \
                 "/" + database_name

db_engine = create_engine(mysql_jdbc_url, echo=False)

transaction_detail_pd_df = pd.read_csv("C:\\Users\\Pari\\PycharmProjects\\cloudtv_tech_video_demo\\transaction_detail-2019-05-19.csv", delimiter=',', header=0)

print(transaction_detail_pd_df.head(2))

transaction_detail_pd_df.to_sql(name=table_name,
                            con=db_engine,
                            if_exists='append',
                            index=False)

print("Completed. {0}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


