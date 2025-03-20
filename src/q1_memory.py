import json
from collections import Counter, defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Contador para llevar la cuenta de la cantidad de tweets por cada fecha
    date_counter = Counter()
    user_date_counter = defaultdict(Counter)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            # Extraemos la fecha del tweet, convirtiéndola de string a objeto datetime.date
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            # Extraemos el usuario que publicó el tweet
            user = tweet['user']
            date_counter[date] += 1
            # Incrementamos el contador de tweets del usuario en esa fecha específica
            user_date_counter[date][user] += 1
    top_dates = [date for date, _ in date_counter.most_common(10)]
    result = []
    for date in top_dates:
        # Obtenemos el usuario con más publicaciones en esa fecha
        user_top = user_date_counter[date].most_common(1)[0][0]
        result.append((date, user_top))
    # Retornamos la lista con las 10 fechas más activas y el usuario más activo en cada una de ellas
    return result
