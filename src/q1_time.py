import pandas as pd
from datetime import datetime
from typing import List, Tuple

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    df = pd.read_json(file_path, lines=True)
    # Convierte la columna date del dataframe a tipo datetime solo con la fecha sin hora
    df['date'] = pd.to_datetime(df['date']).dt.date
    #Obtiene el Top 10 de fechas con mas tweets.
    top_dates = df['date'].value_counts().head(10).index.tolist()
    result = []
    for date in top_dates:
         # obtiene el usuario que mas tweets tiene en esa fecha 
        usuario_top = df[df['date'] == date]['user'].value_counts().idxmax()
        result.append((date, usuario_top))
    return result