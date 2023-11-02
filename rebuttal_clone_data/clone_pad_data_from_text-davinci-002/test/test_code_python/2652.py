def solution():
    cost_per_kilogram_nuts = 12
    cost_per_kilogram_dried_fruit = 8
    kilograms_of_nuts = 3
    kilograms_of_dried_fruit = 2.5
    cost_of_purchase = (cost_per_kilogram_nuts * kilograms_of_nuts) + (cost_per_kilogram_dried_fruit * kilograms_of_dried_fruit)
    result = cost_of_purchase
    return result

print(solution())