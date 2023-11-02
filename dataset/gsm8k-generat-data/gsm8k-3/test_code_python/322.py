def solution():
    """Austin bought his seven friends each a robot. Each robot costs $8.75. He was charged $7.22 total for tax. He left with $11.53 in change. How much did Austin start with?"""
    # Define the cost and tax of each robot
    ROBOT_COST = 8.75
    TAX_RATE = 0.0875

    # Calculate the total cost of the robots
    total_cost = ROBOT_COST * 7

    # Calculate the amount of tax charged
    tax = total_cost * TAX_RATE

    # Calculate the amount paid by Austin
    paid = total_cost + tax

    # Calculate Austin's starting amount
    starting_amount = paid + 11.53

    # Display Austin's starting amount
    result = starting_amount
    return result

print(solution())