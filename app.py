import os
from dash import Dash
import dash_bootstrap_components as dbc
import polars as pl
from layout import create_layout
from callbacks import register_callbacks
from init_db import init_db

def create_app(df: pl.DataFrame) -> Dash:
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "Wines Dash App"
    app.layout = create_layout(df)
    register_callbacks(app, df)
    return app

if __name__ == '__main__':
    init_db()
    df = pl.read_csv("data/prepared_data.csv")
    app = create_app(df)
    port = int(os.environ.get("PORT", 8050))
    app.run_server(host="0.0.0.0", port=port)