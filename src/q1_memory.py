import json
from collections import Counter, defaultdict
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_counter = Counter()
    user_date_counter = defaultdict(Counter)
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet['user']
            date_counter[date] += 1
            user_date_counter[date][user] += 1
    top_dates = [date for date, _ in date_counter.most_common(10)]
    result = []
    for date in top_dates:
        user_top = user_date_counter[date].most_common(1)[0][0]
        result.append((date, user_top))
    return result