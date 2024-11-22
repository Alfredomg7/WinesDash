import dash_bootstrap_components as dbc

def create_checklist(id: str, options: list[dict], value: list[str]) -> dbc.Checklist:
    checklist = dbc.Checklist(
        id=id,
        options=options,
        value=value,
        inline=True
    )
    return checklist