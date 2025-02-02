import requests
from re import IGNORECASE, search
from hashlib import sha256

TIMEOUT = 10
DATA_URL = "https://data.nola.gov/api/views/en36-xvxg/rows.csv"
NAME = r"Declouet"
ADDR = r"321 S Pierce"
KNOWN_HASHES = [
    "0c0b03ed3d50e260e2aa6bf1bb901c34f77706653240520fd9feaaac6b923770",
    "9a24808b18b5974b7c3c1c1aaf77d28af54945cb3b44c8cfbbbca421010ee590",
]

def marta():
    res = requests.get(DATA_URL, timeout=TIMEOUT)
    res.raise_for_status()
    for line in res.text.splitlines():
        if search(NAME, line, flags=IGNORECASE):
            if sha256(line.encode()).hexdigest() not in KNOWN_HASHES:
                print(f"CHANGE: {line}")
                print(f"new hash: {sha256(line.encode()).hexdigest()}")


if __name__ == '__main__':
    marta()
