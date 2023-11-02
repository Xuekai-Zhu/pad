def solution():
    """Jackson wants to impress his girlfriend by filling her hot tub with champagne. The hot tub holds 40 gallons of liquid. Each bottle of champagne holds 1 quart. (There are 4 quarts per gallon). If each bottle of champagne costs $50, but Jackson gets a 20% volume discount, how much does he spend on champagne?"""
    hot_tub_size = 40 * 4 # convert gallons to quarts
    bottle_size = 1 # quart
    bottle_cost = 50
    discount_percent = 20
    total_bottles = hot_tub_size / bottle_size
    discounted_total_cost = total_bottles * bottle_cost * (1 - discount_percent/100)
    result = discounted_total_cost
    return result

print(solution())