def solution():
    """Neil charges $5.00 to trim up each boxwood. He charges $15.00 to trim it into a fancy shape. The customer wants the entire 30 boxwood hedge trimmed up. He has also asked for 4 specific boxwoods shaped into spheres. How much will Neil charge?"""
    num_boxwood = 30
    sphere_boxwood = 4
    trim_price = 5
    fancy_price = 15

    total_trim_cost = num_boxwood * trim_price
    total_fancy_cost = (num_boxwood - sphere_boxwood) * trim_price + sphere_boxwood * fancy_price

    total_cost = total_trim_cost + total_fancy_cost
    result = total_cost
    return result

print(solution())