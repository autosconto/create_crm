import sys
import os

# Aggiungi la root del progetto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import app

