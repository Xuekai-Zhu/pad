def solution():
    """Jasmine bought 4 pounds of coffee beans and 2 gallons of milk. A pound of coffee beans costs $2.50 and a gallon of milk costs $3.50. How much will Jasmine pay in all?"""
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