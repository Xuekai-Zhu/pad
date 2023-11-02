def solution():
    """Kyle bikes for 2 hours to work every day. Ten times the time he takes to travel to work and back is the same as the cost of buying a pack of snacks (in dollars). How much will Ryan pay, in dollars, to buy 50 packs of snacks?"""
    # Define the time it takes for Kyle to travel to work and back
    total_time = 2 * 2

    # Calculate the cost of one pack of snacks
    snack_cost = total_time * 10

    # Calculate the cost of buying 50 packs of snacks
    total_cost = snack_cost * 50

    result = total_cost
    return result

print(solution())