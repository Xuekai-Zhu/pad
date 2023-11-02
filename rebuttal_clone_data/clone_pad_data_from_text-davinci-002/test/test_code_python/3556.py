def solution():
     episodes_bought = 50
     episodes_watched_per_day = episodes_bought / 10
     days_needed = episodes_bought / episodes_watched_per_day
     result = days_needed
     return result

print(solution())