def solution():
    """James decides to buy two suits.  The first is an off-the-rack suit which costs $300.  The second is a tailored suit that costs three as much plus an extra $200 for tailoring.  How much did he pay for both suits?"""
    # Define the cost of the off-the-rack suit
    off_the_rack_cost = 300

    # Define the cost multiplier for the tailored suit
    tailored_cost_multiplier = 3

    # Define the additional cost for tailoring the tailored suit
    tailoring_cost = 200

    # Calculate the cost of the tailored suit
    tailored_cost = (off_the_rack_cost * tailored_cost_multiplier) + tailoring_cost

    # Calculate the total cost of both suits
    total_cost = off_the_rack_cost + tailored_cost

    result = total_cost
    return result

print(solution())