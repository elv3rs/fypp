import os
from pathlib import Path

# Tests assume CWD is the test/ directory (include paths, input files, etc.)
os.chdir(Path(__file__).resolve().parent)
