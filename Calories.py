#El siguiente codigo tiene como finalidad sacar un promedio diario de calorias consumidas por el usuario utilizando un archivo JSON
from google.colab import files
import json

uploaded = files.upload()

file_name = "Name.json"


with open(file_name, "r") as json_file:
    data = json.load(json_file)

# Inicializa una variable para almacenar el total de calorías
total_calories = 0

# Itera sobre los registros diarios para sumar las calorías de comida y actividad
for day in data["dailyLogs"]:
    # Suma las calorías de la comida
    food_calories = sum(food_log["nutrients"]["kcal"] for food_log in day["foodLogs"])
    # Suma las calorías de la actividad
    activity_calories = sum(log["calories"] for log in day["activityLogs"])
    # Suma las calorías totales del día (comida + actividad)
    total_calories += food_calories + activity_calories

# Calcula el promedio de calorías por día durante 7 días
average_calories_per_day = total_calories / 7

print("Promedio de calorías por día durante 7 días:", average_calories_per_day)

