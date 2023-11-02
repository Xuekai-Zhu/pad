def solution():
     laps_per_night = 5
     days = 5
     feet_per_lap = 100
     feet_per_calorie = 25
     total_feet = laps_per_night * days * feet_per_lap
     total_calories = total_feet / feet_per_calorie
     result = total_calories
 
     return result

print(solution())