import os
import sys
import pathlib
import warnings

BASE_DIR = pathlib.Path("__file__").resolve().parent

DATASET_DIR = os.path.join(BASE_DIR, "dataset")

DATASET = os.path.join(BASE_DIR, "dataset", "loan.zip")

EXTRACTED_DIR = os.path.join(BASE_DIR, "extracted_data")


def extract_data(data: str) -> bool:
    try:
        import zipfile
    except Exception as e:
        warnings.warn(f"Error: {e}")
        sys.exit(1)
    
    try:
        with zipfile.ZipFile(data, 'r') as zipfile:
            zipfile.extractall(EXTRACTED_DIR)
    except Exception as e:
        warnings.warn(f"Error: {e}")
        sys.exit(1)
    return True