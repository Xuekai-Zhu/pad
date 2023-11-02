def solution():
    """There are four lamps in Valerie's room. All of them are burnt out, so she needs to buy new light bulbs. She needs 3 small light bulbs and 1 large light bulb. She has $60 to spend. If small light bulbs cost $8 and large light bulbs cost $12, how much money will Valerie have left over?"""
    # Define the cost of each type of light bulb
    SMALL_BULB_COST = 8
    LARGE_BULB_COST = 12

    # Define the number of each type of light bulb required
    small_bulbs = 3
    large_bulbs = 1

    # Calculate the total cost of the light bulbs
    total_cost = (small_bulbs * SMALL_BULB_COST) + (large_bulbs * LARGE_BULB_COST)

    # Calculate the amount of money left over
    left_over = 60 - total_cost

    # Display the amount of money left over
    result = left_over
    return result

print(solution())