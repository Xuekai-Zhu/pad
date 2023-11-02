def solution():
     victor_weight = 126
     bear_weight = 90
     days_in_week = 7
     weeks_in_hibernation = 3
     total_food = (bear_weight * days_in_week * weeks_in_hibernation) / victor_weight
     result = total_food
     return result

print(solution())