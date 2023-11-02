def solution():
    """
    Shannon bought 5 pints of frozen yogurt, two packs of chewing gum, 
    and five trays of jumbo shrimp from The Food Place for a total of $55 
    If the price of a tray of jumbo shrimp is $5 and a pack of chewing gum costs 
    half as much as a pint of frozen yogurt, what is the price of a pint of frozen yogurt?
    """
    total_cost = 55
    num_froyo = 5
    num_gum = 2
    num_shrimp = 5
    price_shrimp = 5
    price_gum = 0.5 * price_froyo
    total_froyo_cost = total_cost - (num_shrimp * price_shrimp) - (num_gum * price_gum)
    price_froyo = total_froyo_cost / num_froyo
    result = price_froyo
    return result

print(solution())