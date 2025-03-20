import pandas as pd
import re
from collections import Counter
from typing import List, Tuple

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # Se carga todo el archivo JSON en un dataframe de pandas
    df = pd.read_json(file_path, lines=True)
    mentions = Counter()
    for content in df['content']:
        # Se buscan todas las menciones que empiecen con @ seguidas de letras, números o guiones bajos
        mentions.update(re.findall(r'@(\w+)', content))
    return mentions.most_common(10)