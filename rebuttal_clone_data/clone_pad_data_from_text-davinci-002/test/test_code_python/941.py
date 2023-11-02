def solution():
    pictures_taken_per_day = 10
    days_per_year = 365
    years = 3
    pictures_taken_total = pictures_taken_per_day * days_per_year * years
    memory_cards_needed = pictures_taken_total / 50
    cost_per_memory_card = 60
    total_cost = memory_cards_needed * cost_per_memory_card
    result = total_cost
    return result

print(solution())