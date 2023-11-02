def solution():
    fraction_per_night = 1/5
    cost_per_bottle = 2.0
    servings_per_bottle = 5

    # Calculate the total number of servings of sparkling water that Mary Anne drinks in a year
    total_servings = 365 * fraction_per_night

    # Calculate the total number of bottles of sparkling water that Mary Anne buys in a year
    total_bottles = total_servings / servings_per_bottle

    # Calculate the total cost of all bottles of sparkling water that Mary Anne buys in a year
    total_cost = total_bottles * cost_per_bottle
    result = total_cost
    return result

print(solution())