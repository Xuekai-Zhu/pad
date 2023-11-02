def solution():
    """Samantha bought a crate of 30 eggs for $5. If she decides to sell each egg for 20 cents, how many eggs will she have left by the time she recovers her capital from the sales?"""
    eggs_in_crate = 30
    cost_of_crate = 5
    price_per_egg = 0.20
    revenue_needed = cost_of_crate
    eggs_sold = 0
    
    # Keep selling eggs until revenue covers the cost of the crate
    while revenue_needed > 0:
        egg_revenue = price_per_egg * (eggs_in_crate - eggs_sold)
        if egg_revenue >= revenue_needed:
            eggs_sold += int(revenue_needed / price_per_egg)
            revenue_needed = 0
        else:
            eggs_sold += eggs_in_crate - eggs_sold
            revenue_needed -= egg_revenue
            
    eggs_left = eggs_in_crate - eggs_sold
    result = eggs_left
    return result

print(solution())