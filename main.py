import requests
from loguru import logger
import json


logger.add("hello.log", rotation="500 MB", retention="10 days", level="INFO")


def get_data():
    r = requests.get('https://results.sos.ga.gov/cdn/results/Georgia/export-2024NovGen.json')
    logger.info(f"Status code: {r.status_code}")
    with open('output.json', 'w') as f:
        f.write(r.text)
    return r.json()


def main():
    data = get_data()
    logger.info(data)
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    main()
