from sqlalchemy import create_engine

def get_connection():
    engine = create_engine("postgresql://postgres:root@localhost:5432/analise_agro")
    return engine