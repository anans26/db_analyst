from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg2://postgres:postgres@localhost:5433/logistics_ai"
)

engine = create_engine(DATABASE_URL)