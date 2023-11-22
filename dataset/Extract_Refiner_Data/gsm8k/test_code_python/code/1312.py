def solution():
    
    # Define the initial cost of the radiator
    initial_cost = 400

    # Calculate the discounted cost of the radiator
    discounted_cost = initial_cost * 0.2

    # Calculate the total cost of the radiator with the discount
    total_cost = discounted_cost * 3

    # Calculate the cost of the mechanic
    mechanic_cost = 50 * 3

    # Calculate the total cost including the mechanic
    total_cost += mechanic_cost

    # return the result
    result = total_cost
    return result

print(solution())