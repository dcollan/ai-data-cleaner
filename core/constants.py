import os
from pathlib import Path

JOB_STATUS_TRANSITIONS = {
    "pending": ["profiling"],
    "profiling": ["suggesting", "failed"],
    "suggesting": ["applying", "failed"],
    "applying": ["done", "failed"],
    "done": [],
    "failed": ["profiling"],  # 👈 retry allowed
}

# Use project-local data directory for local development
if os.getenv("DATA_DIR"):
    DATA_DIR = os.getenv("DATA_DIR")
else:
    project_root = Path(__file__).resolve().parents[1]
    DATA_DIR = str(project_root / "data")
