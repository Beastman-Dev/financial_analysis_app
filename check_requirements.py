import sys
import importlib.util  # <- Fix: use importlib.util instead of just importlib

REQUIRED_PACKAGES = [
    "pandas",
    "matplotlib"
]

def check_packages():
    missing = []
    for pkg in REQUIRED_PACKAGES:
        if importlib.util.find_spec(pkg) is None:
            missing.append(pkg)
    
    if missing:
        print("Missing required packages:")
        for pkg in missing:
            print(f"  - {pkg}")
        print("\nPlease install them using:")
        print(f"  pip install {' '.join(missing)}")
        sys.exit(1)

if __name__ == "__main__":
    check_packages()
