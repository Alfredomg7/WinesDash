import polars as pl
import plotly.express as px
from utils import style_fig

def create_bar_chart(data: pl.DataFrame, x: str, y: str, title: str,
                     color: str, color_discrete_map: dict = None, barmode: str = 'group') -> px.bar:
    fig = px.bar(data, x=x, y=y, title=title, color=color, 
                 color_discrete_map=color_discrete_map, barmode=barmode,
                 text=y)
    fig.update_traces(
        texttemplate='%{text}',
        textposition='outside',
        hovertemplate='Count: %{y}',
    )
    for trace in fig.data:
        trace.textfont = dict(
            size=16,
            family='Arial',
            color=trace.marker.color,
            weight='bold'
        )
    max_y = data[y].max()
    fig.update_yaxes(range=[0, max_y * 1.1])
    style_fig(fig, title)
    return fig