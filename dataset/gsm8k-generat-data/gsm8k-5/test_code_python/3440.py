def solution():
    # Calculate the cost of the pasta
    pasta_cost = 2 * 1.5  # 2 kilograms of pasta at $1.5 per kilogram

    # Calculate the cost of the ground beef
    ground_beef_cost = (1/4) * 8  # 1/4 kilogram of ground beef at $8 per kilogram

    # Calculate the cost of the pasta sauce
    pasta_sauce_cost = 2 * 2  # Two jars of pasta sauce at $2 per jar

    # Calculate the total cost
    total_cost = pasta_cost + ground_beef_cost + pasta_sauce_cost + 6  # Plus $6 for the Quesadilla

    result = total_cost
    return result

print(solution())