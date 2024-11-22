import polars as pl
import plotly.express as px
from utils import style_fig

def create_scatter_chart(data: pl.DataFrame, x: str, y: str, title: str,
                         color: str, color_discrete_map: dict = None) -> px.scatter:
    fig = px.scatter(data, x=x, y=y, title=title, color=color, color_discrete_map=color_discrete_map)
    fig.update_traces(
        marker=dict(size=12, 
                    line=dict(width=1, color='white'),
                ),
        hovertemplate='Year: %{x}<br>Count: %{y}'
    )
    style_fig(fig, title)
    return fig