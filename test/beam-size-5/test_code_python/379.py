def solution():
    
    supplies_cost = 18
    pitchers_of_lemonade = 3
    cups_per_pitcher = 12
    cups_of_lemonade = pitchers_of_lemonade * cups_per_pitcher
    price_per_cup = 1
    cups_sold_per_hour = 4
    total_cups_sold = cups_of_lemonade * price_per_cup
    profit_per_hour = total_cups_sold / total_cups_sold
    result = profit_per_hour
    return result

print(solution())