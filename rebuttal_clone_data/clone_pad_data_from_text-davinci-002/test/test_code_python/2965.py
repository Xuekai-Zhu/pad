def solution():
    costco_gallon_cost = 8
    number_of_ounces_in_gallon = 128
    ounces_in_bottle = 16
    number_of_bottles_in_gallon = number_of_ounces_in_gallon / ounces_in_bottle
    cost_per_bottle = 3
    total_cost_of_bottles = number_of_bottles_in_gallon * cost_per_bottle
    savings = total_cost_of_bottles - costco_gallon_cost
    result = savings
    return result

print(solution())