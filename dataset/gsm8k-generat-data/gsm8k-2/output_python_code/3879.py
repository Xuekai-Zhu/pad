def solution():
    """Chester must deliver ten bales of hay to Farmer Brown. Farmer Brown wants Chester to supply better quality hay and double the delivery of bales of hay. If the previous hay cost $15 per bale, and the better quality one cost $18 per bale, how much more money will Farmer Brown need to meet his own new requirements?"""
    num_bales = 20
    prev_hay_price = 15
    better_hay_price = 18
    prev_hay_total_cost = num_bales * prev_hay_price
    better_hay_total_cost = num_bales * better_hay_price
    extra_cost = better_hay_total_cost - prev_hay_total_cost
    result = extra_cost
    return result

print(solution())