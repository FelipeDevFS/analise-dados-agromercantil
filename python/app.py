import pandas as pd
from database import get_connection

engine = get_connection()

df = pd.read_sql("SELECT * FROM pedidos", engine)

print(df.head())