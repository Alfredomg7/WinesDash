import plotly.graph_objects as go

def style_fig(fig: go.Figure, title: str) -> go.Figure:
    fig.update_layout(
        template='plotly_dark',
        title=dict(
            text=title,
            font=dict(size=24, family='Arial'),
            x=0.5,
        ),
        xaxis=dict(
            title_font=dict(size=20, family='Arial'),
            showgrid=False,
        ),
        yaxis=dict(
            title_font=dict(size=20, family='Arial'),
            showgrid=True
        ),
        margin=dict(l=40, r=40, t=50, b=30),
    )
    return fig