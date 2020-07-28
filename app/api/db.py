import os

import pandas as pd
from databases import Database
from sqlalchemy import (Column, Integer, Float, MetaData, String, Table,
                        create_engine, ARRAY)

# read outlet data
OUTLET_DATA_PATH = "/app/data/UK_outlet_meal.parquet.gzip"

outlet_data = pd.read_parquet(
    os.path.join("file://localhost/", OUTLET_DATA_PATH),
    engine="fastparquet"
)

# specify AWS database URL
DATABASE_URL = 'postgresql://postgres:password@dashmote-db.clezwtvgxfwg.eu-west-1.rds.amazonaws.com/postgres'

engine = create_engine(DATABASE_URL)

metadata = MetaData()

metadata.bind = engine

metadata.create_all(engine)

regex_matches = Table(
    'regex_matches',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('regex_query', String(100)),
    Column('search_word', String(100)),
    Column('num_outlets', Integer),
    Column('per_outlets', Float(precision=2)),
    Column('brand_id', ARRAY(String))
)

database = Database(DATABASE_URL)