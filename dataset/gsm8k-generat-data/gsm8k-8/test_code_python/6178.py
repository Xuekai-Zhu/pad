def solution():
    # Define the total cost and the amount of money Ibrahim has
    total_cost = 120 + 19
    savings = 55

    # Add the father's contribution
    savings += 20

    # Calculate the amount of money Ibrahim needs to purchase the items
    remaining_cost = total_cost - savings

    # Return the result
    result = remaining_cost
    return result

print(solution())