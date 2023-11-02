def solution():
    price_per_pencil = 0.2
    num_pencils_tolu = 3
    num_pencils_robert = 5
    num_pencils_melissa = 2

    # Calculate the total cost for Tolu's pencils
    total_cost_tolu = num_pencils_tolu * price_per_pencil

    # Calculate the total cost for Robert's pencils
    total_cost_robert = num_pencils_robert * price_per_pencil

    # Calculate the total cost for Melissa's pencils
    total_cost_melissa = num_pencils_melissa * price_per_pencil

    # Calculate the total cost for all the pencils
    total_cost = total_cost_tolu + total_cost_robert + total_cost_melissa
    result = total_cost
    return result

print(solution())