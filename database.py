from pathlib import Path
from sqlalchemy import create_engine

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "investments.db"

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    echo=False
)

def get_engine():
    return engine