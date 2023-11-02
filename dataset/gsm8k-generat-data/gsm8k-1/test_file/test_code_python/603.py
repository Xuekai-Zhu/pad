def solution():
    """The jumbo bottle of shampoo costs $24.00. The directions say to use 2 pumps of shampoo and this will give you 120 washings. If Jackie only uses 1 pump per wash, how much will each pump cost, in cents?"""
    cost = 2400  # cost in cents
    total_washings = 120
    pumps_per_washing = 2
    pumps_per_bottle = total_washings * pumps_per_washing
    cost_per_pump = cost / pumps_per_bottle
    result = cost_per_pump
    return result

print(solution())