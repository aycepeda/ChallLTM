import json, re
from collections import Counter
from typing import List, Tuple

# Se define  un patrón de expresión regular para encontrar menciones en los textos
mention_pattern = re.compile(r'@(\w+)')

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mentions = Counter()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Se carga el tweet como un diccionario
            tweet = json.loads(line)
            #devuelve una lista con todas las menciones encontradas
            mentions.update(mention_pattern.findall(tweet['content']))
    return mentions.most_common(10)