def solution():
    
    daily_harvest = 5
    days_in_april = 30
    total_harvest = daily_harvest * days_in_april
    given_away = 20
    stolen = 30
    remaining_strawberries = total_harvest - given_away - stolen
    result = remaining_strawberries
    return result

print(solution())