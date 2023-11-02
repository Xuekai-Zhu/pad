def solution():
    """This year the Oscar swag bags include two diamond earrings that cost $6,000 each, a new iPhone that costs $2,000, and some designer scarves that each cost $1,500. If the total value of the swag bag is $20,000, how many scarves are there?"""
    # Define the cost of each item
    EARRINGS_COST = 6000
    IPHONE_COST = 2000
    SCARF_COST = 1500

    # Define the number of each item
    earrings_num = 2
    iphone_num = 1

    # Calculate the total cost of the earrings and iPhone
    total_ei_cost = (earrings_num * EARRINGS_COST) + IPHONE_COST

    # Calculate the remaining cost for the scarves
    scarf_cost_remaining = 20000 - total_ei_cost

    # Calculate the number of scarves that can be purchased with the remaining cost
    scarf_num = scarf_cost_remaining // SCARF_COST

    # Display the number of scarves
    result = scarf_num
    return result

print(solution())