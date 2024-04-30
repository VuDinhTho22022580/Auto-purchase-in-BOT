from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


'''
nếu dùng database bằng SQL server
connection = pyodbc.connect(
    'driver={SQL Server};'
    'server=TUANTHANH\\SQLEXPRESS;'
    'database=DBForBOT;'
    'user :TuanThanh;'
    'password=Nttthanh88;'
    'port=1433;'
    )
'''


SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = orm.declarative_base()