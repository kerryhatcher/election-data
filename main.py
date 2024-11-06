import requests
from loguru import logger
import json
import typer


logger.add("vote.log", rotation="500 MB", retention="10 days", level="INFO")


app = typer.Typer()

@app.command()
def hello():
    typer.echo("Hello, World!")

@app.command()
def getdata():
    data = get_data()
    logger.info(data)
    print(json.dumps(data, indent=4))


def get_data():
    r = requests.get('https://results.sos.ga.gov/cdn/results/Georgia/export-2024NovGen.json')
    logger.info(f"Status code: {r.status_code}")
    with open('output.json', 'w') as f:
        f.write(r.text)
    return r.json()




if __name__ == "__main__":
    app()
