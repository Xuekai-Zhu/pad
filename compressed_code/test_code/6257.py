def solution():
    
    iced_tea_per_drink = 1/4
    lemonade_per_drink = 1 + 1/4
    total_cups_per_drink = iced_tea_per_drink + lemonade_per_drink
    total_drinks_in_pitcher = 18 / total_cups_per_drink
    cups_of_lemonade = total_drinks_in_pitcher * lemonade_per_drink
    result = cups_of_lemonade
    return result

print(solution())