def solution():
    """
    Chester must deliver ten bales of hay to Farmer Brown. Farmer Brown wants Chester to supply better quality hay
    and double the delivery of bales of hay. If the previous hay cost $15 per bale, and the better quality one cost $18
    per bale, how much more money will Farmer Brown need to meet his own new requirements?
    """
    num_bales = 20  # Double the original amount of bales
    cost_per_bale_old = 15
    cost_per_bale_new = 18
    cost_old = num_bales * cost_per_bale_old
    cost_new = num_bales * cost_per_bale_new
    additional_cost = cost_new - cost_old
    result = additional_cost
    return result

print(solution())