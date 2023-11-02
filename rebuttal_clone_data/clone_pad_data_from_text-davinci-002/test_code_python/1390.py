def solution():
    coffees_per_day = 2
    days = 20
    price_of_double_espresso = 3.00
    price_of_iced_coffee = 2.50
    total_price = (coffees_per_day * days * price_of_double_espresso) + (coffees_per_day * days * price_of_iced_coffee)
    result = total_price 
    return result

print(solution())