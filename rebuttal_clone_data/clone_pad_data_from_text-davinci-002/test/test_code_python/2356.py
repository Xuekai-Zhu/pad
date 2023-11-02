def solution():
    days_in_month = 30
    strawberries_harvested = 5
    strawberries_given_away = 20
    strawberries_stolen = 30
    strawberries_left = days_in_month * strawberries_harvested - strawberries_given_away - strawberries_stolen
    result =  strawberries_left
    return result

print(solution())