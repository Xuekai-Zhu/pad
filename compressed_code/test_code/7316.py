def solution():
    
    women_shirts_per_hour = 2
    men_shirts_per_hour = 1.5
    hours_per_day = 12
    days_per_week = 7
    price_per_women_shirt = 18
    price_per_men_shirt = 15
    total_women_shirts_sold = women_shirts_per_hour * hours_per_day * days_per_week
    total_men_shirts_sold = men_shirts_per_hour * hours_per_day * days_per_week
    total_earnings = (total_women_shirts_sold * price_per_women_shirt) + (total_men_shirts_sold * price_per_men_shirt)
    result = total_earnings
    return result

print(solution())