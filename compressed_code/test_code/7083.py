def solution():
    
    pictures_per_day = 10
    days_per_year = 365
    years = 3
    total_pictures = pictures_per_day * days_per_year * years
    pictures_per_card = 50
    cards_needed = total_pictures / pictures_per_card
    cost_per_card = 60
    total_cost = cards_needed * cost_per_card
    result = total_cost
    return result

print(solution())