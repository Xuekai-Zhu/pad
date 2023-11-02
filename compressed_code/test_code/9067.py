def solution():
    
    strawberries_per_day = 5
    days_in_april = 30
    total_strawberries = strawberries_per_day * days_in_april
    strawberries_given_away = 20
    strawberries_stolen = 30
    remaining_strawberries = total_strawberries - strawberries_given_away - strawberries_stolen
    result = remaining_strawberries
    return result

print(solution())