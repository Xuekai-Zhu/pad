def solution():
    # Calculate the total amount of money Austin earns in a week
    money_per_week = 5 * (2 + 1 + 3)  # Austin works for 2 hours on Mondays, an hour on Wednesdays, and 3 hours on Fridays
    
    # Calculate the number of weeks Austin needs to work to earn $180
    weeks_to_work = 180 / money_per_week
    
    result = weeks_to_work
    return result

print(solution())