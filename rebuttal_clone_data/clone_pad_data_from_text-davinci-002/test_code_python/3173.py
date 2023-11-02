def solution():
    cards_bought_per_week = 20
    weeks_per_year = 52
    cards_bought_per_year = cards_bought_per_week * weeks_per_year
    percentage_lost = 50
    cards_lost = cards_bought_per_year * (percentage_lost / 100)
    cards_left = cards_bought_per_year - cards_lost
    result = cards_left
    return result

print(solution())