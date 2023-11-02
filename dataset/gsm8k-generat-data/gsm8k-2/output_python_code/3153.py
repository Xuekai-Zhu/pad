def solution():
    """Every day, Billie bakes 3 pumpkin pies for 11 days and puts them in the refrigerator. It takes 2 cans of whipped cream to cover 1 pie. If Tiffany comes over and eats 4 pies, how many cans of whipped cream does Billie need to buy to cover the remaining pies?"""
    pies_per_day = 3
    total_days = 11
    total_pies = pies_per_day * total_days
    whipped_cream_per_pie = 2
    eaten_pies = 4
    remaining_pies = total_pies - eaten_pies
    total_whipped_cream = remaining_pies * whipped_cream_per_pie
    result = total_whipped_cream
    return result

print(solution())