def solution():
    """Five shirts together cost $85. Of the 5 shirts, there are 3 shirts that cost $15 each. If the remaining shirts are each equal in value, what is the cost, in dollars, of one of the remaining shirts?"""
    # Define the cost of the three shirts that cost $15 each
    cost_of_three_shirts = 15 * 3

    # Define the total cost of all five shirts
    total_cost = 85

    # Calculate the cost of the remaining two shirts
    cost_of_remaining_two_shirts = total_cost - cost_of_three_shirts

    # Calculate the cost of one of the remaining shirts
    cost_of_one_remaining_shirt = cost_of_remaining_two_shirts / 2

    # Display the cost of one of the remaining shirts
    result = cost_of_one_remaining_shirt
    return result

print(solution())