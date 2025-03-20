import pandas as pd
import emoji
from collections import Counter
from typing import List, Tuple

def q2_time(file_path: str) -> List[Tuple[str, int]]:
     # Se lee el archivo línea por línea como objetos JSON independientes
    df = pd.read_json(file_path, lines=True)
    emojis = Counter()
    for content in df['content']:
         # Se accede al valor del emoji
        emojis.update([e['emoji'] for e in emoji.emoji_list(content)])
    # Retorna el top 10 de los emojis mas comunes junto a su frecuencia
    return emojis.most_common(10)