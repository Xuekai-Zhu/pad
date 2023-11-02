def solution():
    """Kyle bikes for 2 hours to work every day. Ten times the time he takes to travel to work and back is the same as the cost of buying a pack of snacks (in dollars). How much will Ryan pay, in dollars, to buy 50 packs of snacks?"""
    time_per_day = 2 * 2 # to and from work
    cost_per_hour = 10
    cost_per_snack = time_per_day * cost_per_hour * 10
    num_snacks = 50
    total_cost = cost_per_snack * num_snacks
    result = total_cost
    return result

print(solution())