def solution():
    """James decides to buy two suits. The first is an off-the-rack suit which costs $300. The second is a tailored suit that costs three as much plus an extra $200 for tailoring. How much did he pay for both suits?"""
    # Define the cost of the off-the-rack and tailored suits
    off_the_rack_cost = 300
    tailored_cost = (3 * off_the_rack_cost) + 200

    # Calculate the total cost of both suits
    total_cost = off_the_rack_cost + tailored_cost

    result = total_cost
    return result

print(solution())