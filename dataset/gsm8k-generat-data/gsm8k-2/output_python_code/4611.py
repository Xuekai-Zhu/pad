def solution():
    """Samantha bought a crate of 30 eggs for $5. If she decides to sell each egg for 20 cents, how many eggs will she have left by the time she recovers her capital from the sales?"""
    egg_cost = 5
    egg_price = 0.2
    eggs_sold = egg_cost / egg_price
    eggs_left = 30 - eggs_sold
    result = eggs_left
    return result

print(solution())