def solution():
    # Calculate the cost of the pasta
    pasta_weight = 2  # kilograms
    pasta_cost = 1.5 * pasta_weight

    # Calculate the cost of the ground beef
    beef_weight = 0.25  # kilograms
    beef_cost = 8 * beef_weight

    # Calculate the cost of the pasta sauce
    sauce_count = 2
    sauce_cost = 2 * sauce_count

    # Calculate the total cost of the groceries
    total_cost = pasta_cost + beef_cost + sauce_cost

    # Add the cost of the Quesadilla
    total_cost += 6

    result = total_cost
    return result

print(solution())