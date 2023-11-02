def solution():
    
    iced_tea_per_drink = 0.25
    lemonade_per_drink = 1.25
    total_cups_per_drink = iced_tea_per_drink + lemonade_per_drink
    total_drinks = 18 / total_cups_per_drink
    cups_of_lemonade = total_drinks * lemonade_per_drink
    result = cups_of_lemonade
    return result

print(solution())