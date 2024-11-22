import plotly.graph_objects as go

def style_fig(fig: go.Figure, title: str) -> go.Figure:
    fig.update_layout(
        template='plotly_dark',
        title=dict(
            text=title, 
            font=dict(size=24, family='Arial'),
            x=0.5,
            ),
        xaxis_title=None,
        yaxis_title=None,
        showlegend=False,
    )
    return fig