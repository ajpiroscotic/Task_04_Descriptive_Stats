import csv
import math
from collections import defaultdict, Counter

def load_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
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
            if values:  # numeric stats
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
            else:  # categorical stats
                cats = [row[key] for row in rows if row[key]]
                if cats:
                    counts = Counter(cats)
                    group_stats[key] = {
                        'unique_values': len(counts),
                        'most_common': counts.most_common(3)
                    }
        stats[group] = group_stats
    return stats

if __name__ == "__main__":
    file_path = "C:\Users\Anjaneya Padwal\Downloads\coffe.csv"
    data = load_data(file_path)
    overall_stats = descriptive_stats(data)
    print("Overall Stats:", overall_stats)
    stats_by_coffee = descriptive_stats(data, group_by="coffee_name")
    print("Grouped by coffee_name:", list(stats_by_coffee.items())[:2])
