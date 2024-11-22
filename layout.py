from dash import html, dcc
import dash_bootstrap_components as dbc
import polars as pl
import components as cmp
from services import get_categories

def create_layout(df: pl.DataFrame) -> dbc.Container:
    title = html.H1("France vs Italy Wine Comparison", className="text-center text-light")
    description = html.P("Visualize a dataset of over 5,000 PDO wines from Italy and France.")
    link = html.A(
                "Data Source",
                href="https://www.sciencedirect.com/science/article/pii/S2352340924003779",
                target="_blank",
                className="btn btn-light text-nowrap"
                )

    categories_list = get_categories(df)
    category_options = [{"label": category, "value": category} for category in categories_list]
    category_filter = cmp.create_checklist(
        id="category-filter",
        options=category_options,
        value=[]
    )

    distribution_chart = dcc.Graph(id="wine-color-distribution")
    trend_chart = dcc.Graph(id="registration-trend")

    layout = dbc.Container([
            dbc.Row([
                dbc.Col(
                    title,
                    lg=4, md=12, className="text-center mb-2 mb-lg-0"
                ),
                dbc.Col(
                    description,
                    lg=5, md=12, className="text-center"
                ),
                dbc.Col(
                    link,
                    lg=3, md=12, className="text-center mt-2 mt-lg-0"
                ),
            ],
            className="align-items-center mb-4"
            ),
            dbc.Row([
                dbc.Col([
                        html.Label("Select Wine Categories:", className="fw-bold"),
                        category_filter,
                    ],
                    width=12,
                    className="mb-4",
                ),
            ],
            className="mb-4"
            ),
            dbc.Row([
                dbc.Col(distribution_chart, lg=6, md=12, className="mb-4"),
                dbc.Col(trend_chart, lg=6, md=12, className="mb-4"),
            ],
            className="mb-4"
            ),
        ],
        fluid=True,
        className="bg-dark text-light p-4",
        style={"height": "100%"}
    )
    return layout