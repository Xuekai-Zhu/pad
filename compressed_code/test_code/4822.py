def solution():
    
    drip_coffee_price = 2.25
    double_shot_price = 3.50
    latte_price = 4.00
    vanilla_syrup_price = 0.50
    cold_brew_price = 2.50
    cappuccino_price = 3.50
    total_price = (2 * drip_coffee_price) + double_shot_price + (2 * latte_price) + vanilla_syrup_price + (2 * cold_brew_price) + cappuccino_price
    result = total_price
    return result

print(solution())