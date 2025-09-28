import csv
import math
from collections import defaultdict, Counter

def load_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def to_float(value):
    try:
        return float(value)
    except:
        return None

def descriptive_stats(data, group_by=None):
    stats = {}
    grouped_data = defaultdict(list)

    # Group data if group_by is specified
    if group_by:
        for row in data:
            grouped_data[row[group_by]].append(row)
    else:
        grouped_data['all'] = data

    for group, rows in grouped_data.items():
        group_stats = {}
        for key in rows[0].keys():
            values = [to_float(row[key]) for row in rows if to_float(row[key]) is not None]
            if not values:
                continue
            count = len(values)
            mean = sum(values) / count
            min_val = min(values)
            max_val = max(values)
            variance = sum((x - mean) ** 2 for x in values) / count
            std_dev = math.sqrt(variance)
            group_stats[key] = {
                'count': count,
                'mean': mean,
                'min': min_val,
                'max': max_val,
                'std_dev': std_dev
            }
        stats[group] = group_stats
    return stats

if __name__ == "__main__":
    file_path = "Stores.csv"
    data = load_data(file_path)
    overall_stats = descriptive_stats(data)
    print("Overall Stats:", overall_stats)
    stats_by_store = descriptive_stats(data, group_by="Store ID ")
    print("Grouped by Store ID:", list(stats_by_store.items())[:2])
