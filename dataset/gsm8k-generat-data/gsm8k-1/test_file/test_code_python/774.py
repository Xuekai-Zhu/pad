def solution():
    """At the local Pick Your Own fruit orchard, you could pick your own peaches for $2.00 per pound, plums were $1.00 per pound and apricots were $3.00 per pound. If Winston picked 6 pounds of peaches, 8 pounds of plums and 6 pounds of apricots, how much did he spend on fruit?"""
    price_per_pound_peaches = 2.00
    price_per_pound_plums = 1.00
    price_per_pound_apricots = 3.00
    pounds_of_peaches = 6
    pounds_of_plums = 8
    pounds_of_apricots = 6
    total_cost = (price_per_pound_peaches * pounds_of_peaches) + (price_per_pound_plums * pounds_of_plums) + (price_per_pound_apricots * pounds_of_apricots)
    result = total_cost
    return result

print(solution())