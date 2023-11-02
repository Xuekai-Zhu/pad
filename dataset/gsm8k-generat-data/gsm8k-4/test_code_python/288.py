def solution():
    """John decides to get gym memberships so he can get in shape. The gym close to his house is close but doesn't have everything he wants so he gets two different gym memberships. The cheap one costs $10 a month and has a sign-up fee of $50. The second gym is 3 times more expensive and it has a sign-up fee of 4 months membership. How much total did he pay in the first year for gym membership?"""
    # Define the cost of the cheap gym membership
    cheap_membership_cost = 10*12 + 50

    # Define the cost of the expensive gym membership
    expensive_membership_cost = 3 * (10*12) + 4*(10*12)

    # Calculate the total cost of both gym memberships for the first year
    total_cost = cheap_membership_cost + expensive_membership_cost

    result = total_cost
    return result

print(solution())