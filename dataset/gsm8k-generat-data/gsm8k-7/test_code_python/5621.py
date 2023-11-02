def solution():
    total_hours_worked = 8*3 + 5.5*2 
    # Calculate the total hours worked in a week (assuming a 5-day workweek)
    # Divide by 5 to get the average hours worked per day
    hours_per_day = total_hours_worked / 5
    result = hours_per_day
    return result

print(solution())