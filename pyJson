#The next python code takes a JSON file and counts the user's most frequent registrations and sorts it from most to least amount of consumption.
from google.colab import files
import json
from collections import Counter

uploaded = files.upload()


file_name = list(uploaded.keys())[0]

with open(file_name) as f:
    data = json.load(f)

foods = []
for daily_logs in data['dailyLogs']:
    for food in daily_logs['foodLogs']:
        foods.extend(food['food'])

counter = Counter(foods)

ordered_foods = sorted(counter.items(), key=lambda x: x[1], reverse=True)

print("Most repeated foods:")
for foods, repetitions in ordered_foods:
    print(f"'{foods}' with {repetitions} logs.")
