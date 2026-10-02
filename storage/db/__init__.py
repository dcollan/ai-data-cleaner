from .models import Base
from sqlalchemy import create_engine
import os
from pathlib import Path

# Use /tmp on Cloud Run, local data/ directory during development
if os.getenv("DATABASE_URL"):
    database_url = os.getenv("DATABASE_URL")
else:
    project_root = Path(__file__).resolve().parents[2]
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    database_url = f"sqlite:///{data_dir / 'data.db'}"

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False}
)