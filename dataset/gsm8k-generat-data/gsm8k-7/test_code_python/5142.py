def solution():
    doors_to_paint = 8
    pints_per_door = 2
    pint_cost = 8.0
    gallon_cost = 55.0

    # Calculate the total pints needed to paint all doors
    total_pints = doors_to_paint * pints_per_door

    # Calculate the total cost of buying pints individually
    pints_cost = total_pints * pint_cost

    # Calculate the cost of buying a gallon
    gallon_savings = pints_cost - gallon_cost
    result = round(gallon_savings, 2)
    return result

print(solution())