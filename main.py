import os
from src.download.data import Data


os.system("python -m venv .venv")
os.system("source ./venv/bin/activate")
os.system("python setup.py install")
os.system("mkdir output && cd output")


def main():
    Data().dl_data()


if __name__ == "__main__":
    main()
