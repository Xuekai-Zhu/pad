def solution():
    """Kyle bikes for 2 hours to work every day. Ten times the time he takes to travel to work and back is the same as the cost of buying a pack of snacks (in dollars). How much will Ryan pay, in dollars, to buy 50 packs of snacks?"""
    travel_time = 2 * 2 # round trip
    snack_cost = travel_time * 10
    num_snacks = 50
    total_cost = snack_cost * num_snacks
    result = total_cost
    return result

print(solution())