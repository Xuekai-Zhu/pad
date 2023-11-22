def solution():
    
    # Define the initial cost of onions and the number of servings
    initial_cost = 2 * 2
    servings = 6

    # Calculate the cost per serving
    cost_per_serving = initial_cost / servings

    # Calculate the cost per box of beef stock
    cost_per_box = 2 * 2

    # Round the cost per serving to the nearest integer
    rounded_cost = round(cost_per_serving)

    # return the result
    result = rounded_cost
    return result

print(solution())