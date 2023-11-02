def solution():
    """Five shirts together cost $85. Of the 5 shirts, there are 3 shirts that cost $15 each. If the remaining shirts are each equal in value, what is the cost, in dollars, of one of the remaining shirts?"""
    # Define the total cost of the shirts and the cost of the three shirts that cost $15 each
    total_cost = 85
    three_shirt_cost = 15 * 3

    # Calculate the cost of the remaining two shirts
    remaining_cost = total_cost - three_shirt_cost

    # Calculate the cost of one of the remaining shirts
    one_shirt_cost = remaining_cost / 2

    # return the result
    result = one_shirt_cost
    return result

print(solution())