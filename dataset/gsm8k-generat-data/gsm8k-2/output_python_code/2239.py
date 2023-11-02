def solution():
    """Shannon bought 5 pints of frozen yogurt, two packs of chewing gum, and five trays of jumbo shrimp from The Food Place for a total of $55 If the price of a tray of jumbo shrimp is $5 and a pack of chewing gum costs half as much as a pint of frozen yogurt, what is the price of a pint of frozen yogurt?"""
    total_cost = 55
    num_frozen_yogurt = 5
    num_chewing_gum = 2
    num_jumbo_shrimp = 5

    gum_price = 0.5 * (total_cost - num_frozen_yogurt * price_frozen_yogurt - num_jumbo_shrimp * price_jumbo_shrimp) / num_chewing_gum
    price_frozen_yogurt = (total_cost - num_chewing_gum * gum_price - num_jumbo_shrimp * price_jumbo_shrimp) / num_frozen_yogurt
    result = price_frozen_yogurt
    return result

print(solution())