from __future__ import annotations

from typing import Final, Any

from flask import Flask, render_template


app = Flask(__name__)

PARAMETERS: Final[list[dict[str, Any]]] = [
    {"id": 1, "title": "humidity", "unit": "%"},
    {"id": 2, "title": "particles", "unit": "uq"},
    {"id": 3, "title": "temperature", "unit": "°C"},
]


@app.route("/")
def hello_world() -> Any:
    return render_template("home.html", parameters=PARAMETERS)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
