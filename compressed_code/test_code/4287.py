def solution():
    
    coffee_price = 2.5
    milk_price = 3.5
    coffee_weight = 4
    milk_volume = 2
    total_coffee_price = coffee_weight * coffee_price
    total_milk_price = milk_volume * milk_price
    total_price = total_coffee_price + total_milk_price
    result = total_price
    return result

print(solution())