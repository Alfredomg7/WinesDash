import polars as pl
import plotly.express as px
from utils import style_fig

def create_bar_chart(data: pl.DataFrame, x: str, y: str, title: str,
                     color: str, color_discrete_map: dict = None) -> px.bar:
    fig = px.bar(data, x=x, y=y, title=title, color=color, color_discrete_map=color_discrete_map)
    fig.update_traces(
        marker=dict(
            line=dict(width=1, color='DarkSlateGrey'),
            opacity=0.9
        ),
        hovertemplate='Count: %{y}'
    )
    style_fig(fig, title)
    return fig