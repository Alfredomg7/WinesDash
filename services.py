import polars as pl

def filter_by_category(df: pl.DataFrame, categories: list[str]) -> pl.DataFrame:
    if not categories:
        return df
    return df.filter(df['Category'].is_in(categories))

def group_by_country_and_color(df: pl.DataFrame) -> pl.DataFrame:
    return df.group_by(['Country', 'Color']).agg([
        pl.count('Color').alias('Count')
    ])

def group_by_country_and_year(df: pl.DataFrame) -> pl.DataFrame:
    df = df.group_by(['Country', 'Registration Year']).agg([
        pl.count('Registration Year').alias('Count')
    ])
    df = df.with_columns(
        df['Registration Year'].cast(pl.Utf8)
    )
    return df.sort('Registration Year')

def get_categories(df: pl.DataFrame) -> list[str]:
    categories = df['Category'].unique().to_list()
    categories = [category for category in categories if category]
    return sorted(categories)