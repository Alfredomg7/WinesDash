from dash import Dash
import dash_bootstrap_components as dbc
from layout import layout
from callbacks import register_callbacks

def create_app() -> Dash:
    app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "Wines Dash App"
    app.layout = layout
    register_callbacks(app)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run_server(debug=True)