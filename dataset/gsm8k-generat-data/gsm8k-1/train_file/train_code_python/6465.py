def solution():
    """It’s spring! The gardener at Parc Municipal orders flowers. He takes 250 tulips, 375 carnations and 320 roses. Each flower is sold for 2€. Calculate the total expenses."""
    tulips = 250
    carnations = 375
    roses = 320
    price_per_flower = 2
    total_expenses = (tulips + carnations + roses) * price_per_flower
    result = total_expenses
    return result

print(solution())