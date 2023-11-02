def solution():
    """Blake bought 4 lollipops and 6 packs of chocolate. If each lollipop costs $2 and a pack of chocolate costs the same as four lollipops, how much change will Blake get back if he gave the cashier 6 $10 bills?"""
    num_lollipops = 4
    num_chocolate_packs = 6
    cost_per_lollipop = 2
    cost_per_chocolate_pack = cost_per_lollipop * 4
    total_cost = num_lollipops * cost_per_lollipop + num_chocolate_packs * cost_per_chocolate_pack
    amount_paid = 6 * 10
    change = amount_paid - total_cost
    result = change
    return result

print(solution())