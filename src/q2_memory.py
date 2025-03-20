import json, re
from collections import Counter
from typing import List, Tuple

# Se crea un patron de expresion regular para detectar emojis en los textos
emoji_pattern = re.compile("["
                           "😀-🙏"
                           "🌀-🗿"
                           "🚀-🛿"
                           "🜀-🝿"
                           "🞀-🟿"
                           "🠀-🣿"
                           "🤀-🧿"
                           "🨀-🩯"
                           "🩰-🫿"
                           "✂-➰"
                           "Ⓜ-🉑"
                           "]+")
# función para obtener el top 10 de emojis mas usados.
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emojis = Counter()
    # Se abre el archivo línea por línea
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            # devuelve una lista de todos los emojis encontrados en el texto
            # se actualiza el contador de emojis con los encontrados en el tweet actual
            emojis.update(emoji_pattern.findall(tweet['content']))
    return emojis.most_common(10)