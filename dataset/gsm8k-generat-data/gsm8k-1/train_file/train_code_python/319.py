def solution():
    """Austin bought his seven friends each a robot. Each robot costs $8.75. He was charged $7.22 total for tax. He left with $11.53 in change. How much did Austin start with?"""
    num_friends = 7
    cost_per_robot = 8.75
    subtotal = num_friends * cost_per_robot
    total_cost = subtotal + 7.22
    starting_amount = total_cost + 11.53
    result = starting_amount
    return result

print(solution())