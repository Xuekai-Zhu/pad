def solution():
    """Austin bought his seven friends each a robot. Each robot costs $8.75. He was charged $7.22 total for tax. He left with $11.53 in change. How much did Austin start with?"""
    # Define the number of robots and the cost per robot
    num_robots = 7
    cost_per_robot = 8.75

    # Calculate the total cost of the robots
    total_cost = num_robots * cost_per_robot

    # Add the tax to the total cost
    total_cost += 7.22

    # Calculate the amount Austin spent in total
    spent = total_cost + 11.53

    # Calculate how much Austin started with
    start = spent - total_cost

    # return the result
    result = start
    return result

print(solution())