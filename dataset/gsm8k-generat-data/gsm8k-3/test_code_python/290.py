def solution():
    """John decides to get gym memberships so he can get in shape.  The gym close to his house is close but doesn't have everything he wants so he gets two different gym memberships.  The cheap one costs $10 a month and has a sign-up fee of $50.  The second gym is 3 times more expensive and it has a sign-up fee of 4 months membership.  How much total did he pay in the first year for gym membership?"""
    # Calculate the cost of the cheap gym membership for the first year
    cheap_membership_cost = 10 * 12 + 50

    # Calculate the cost of the expensive gym membership for the first year
    expensive_membership_cost = (10 * 3) * 4 + (10 * 3) * 8

    # Calculate the total cost for the first year
    total_cost = cheap_membership_cost + expensive_membership_cost

    # Display the total cost for the first year
    result = total_cost
    return result

print(solution())