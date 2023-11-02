def solution():
    """Tony paid $7 for 2 dozen apples and 1 bunch of bananas. Arnold paid $5 for 1 dozen apples and 1 bunch of bananas. How much does a bunch of bananas cost?"""
    # Define the cost of 1 dozen apples
    dozen_apples_cost = (7 - 1 * 12) / 2

    # Define the cost of 1 bunch of bananas for Tony
    tony_bananas_cost = 7 - dozen_apples_cost * 2

    # Define the cost of 1 bunch of bananas for Arnold
    arnold_bananas_cost = 5 - dozen_apples_cost

    # Calculate the average cost of 1 bunch of bananas
    bananas_cost = (tony_bananas_cost + arnold_bananas_cost) / 2

    # Return the result
    result = bananas_cost
    return result

print(solution())