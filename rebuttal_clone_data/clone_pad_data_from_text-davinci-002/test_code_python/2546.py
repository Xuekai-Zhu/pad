def solution():
     coffee_made = 1.5
     coffee_used = 96
     days = 2
     coffee_left = coffee_made - (coffee_used / days)
     total_days = 24
     total_coffee_needed = (coffee_used / days) * total_days
     total_hours = (total_coffee_needed / coffee_made) * 20
     result = total_hours
     return result

print(solution())