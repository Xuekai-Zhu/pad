def solution():
    """Jackson wants to impress his girlfriend by filling her hot tub with champagne. The hot tub holds 40 gallons of liquid. Each bottle of champagne holds 1 quart. (There are 4 quarts per gallon). If each bottle of champagne costs $50, but Jackson gets a 20% volume discount, how much does he spend on champagne?"""
    hot_tub_capacity = 40 * 4 # convert gallons to quarts
    bottles_needed = hot_tub_capacity / 1 # 1 quart per bottle
    bottle_cost = 50
    discount = 0.2
    total_cost = bottles_needed * bottle_cost * (1 - discount)
    result = total_cost
    return result

print(solution())