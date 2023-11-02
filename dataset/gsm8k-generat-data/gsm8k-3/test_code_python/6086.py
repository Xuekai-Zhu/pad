def solution():
    """John buys 20 candy bars.  His brother Dave pays for 6 of them.  If each candy bar costs $1.50, how much did John pay?"""
    # Define the cost per candy bar
    COST_PER_BAR = 1.5

    # Define the number of candy bars John bought and Dave paid for
    john_bars = 20
    dave_bars = 6

    # Calculate the total cost of the candy bars John bought
    john_cost = (john_bars - dave_bars) * COST_PER_BAR

    # Display the amount John paid
    result = john_cost
    return result

print(solution())