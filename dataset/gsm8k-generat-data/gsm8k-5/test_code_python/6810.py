def solution():
    cakes_per_day = 20  # Brenda bakes 20 cakes per day
    days = 9  # Brenda bakes for 9 days

    # Calculate total number of cakes baked
    total_cakes = cakes_per_day * days

    # Sell half of the cakes
    sold_cakes = total_cakes / 2

    # Calculate how many cakes are left with Brenda
    cakes_left = total_cakes - sold_cakes
    result = cakes_left
    return result

print(solution())