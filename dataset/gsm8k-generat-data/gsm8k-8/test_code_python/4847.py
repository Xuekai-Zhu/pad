def solution():
    # Calculate the total pounds of potato chips needed
    total_pounds = 10 * 1.2

    # Calculate the total cost in cents
    total_cost = total_pounds * 25

    # Convert the total cost to dollars
    total_cost_in_dollars = total_cost / 100

    result = total_cost_in_dollars
    return result

print(solution())