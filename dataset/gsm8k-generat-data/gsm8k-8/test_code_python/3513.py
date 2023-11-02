def solution():
    # Calculate the original fuel cost
    original_cost = 200

    # Calculate the new fuel cost with increased capacity and higher prices
    new_cost = original_cost * 2 * 1.2

    # Round the result to two decimal places and return it
    result = round(new_cost, 2)
    return result

print(solution())