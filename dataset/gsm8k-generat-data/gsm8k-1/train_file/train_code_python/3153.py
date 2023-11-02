def solution():
    """Every day, Billie bakes 3 pumpkin pies for 11 days and puts them in the refrigerator. It takes 2 cans of whipped cream to cover 1 pie. If Tiffany comes over and eats 4 pies, how many cans of whipped cream does Billie need to buy to cover the remaining pies?"""
    pies_per_day = 3
    days_baked = 11
    total_pies = pies_per_day * days_baked
    pies_eaten = 4
    pies_left = total_pies - pies_eaten
    whipped_cream_per_pie = 2
    cans_needed = pies_left * whipped_cream_per_pie
    result = cans_needed
    return result

print(solution())