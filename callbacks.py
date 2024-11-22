from typing import Tuple
import plotly.express as px
import polars as pl
from dash import Dash, Input, Output
import components as cmp
from services import filter_by_category, group_by_country_and_color, group_by_country_and_year

def register_callbacks(app: Dash, df: pl.DataFrame) -> None:
    @app.callback(
        [Output('wine-color-distribution', 'figure'),
        Output('registration-trend', 'figure')],
        [Input('category-filter', 'value')]
    )
    def update_charts(categories: list[str]) -> Tuple[px.bar, px.line]:
        filtered_df = filter_by_category(df, categories)
        color_distribution_df = group_by_country_and_color(filtered_df)
        registration_trend_df = group_by_country_and_year(filtered_df)

        x1 = 'Country'
        y = 'Count'
        color1 = 'Color'
        title1 = 'Wine Color Distribution'

        wines_color_map = {
            'Red': cmp.RED_WINE_COLOR,
            'White': cmp.WHITE_WINE_COLOR,
            'Rose': cmp.ROSE_WINE_COLOR,
        }

        distribution_fig = cmp.create_bar_chart(
            color_distribution_df, x=x1, y=y, color=color1, title=title1, 
            color_discrete_map=wines_color_map
        )

        x2 = 'Registration Year'
        color2 = 'Country'
        title2 = 'Wine Registration Trend Over Time'

        countries_color_map = {
            'France': cmp.FRANCE_COLOR,
            'Italy': cmp.ITALY_COLOR,
        }
        trend_fig = cmp.create_bar_chart(
            registration_trend_df, x=x2, y=y, color=color2, title=title2, 
            color_discrete_map=countries_color_map
        )

        return distribution_fig, trend_fig