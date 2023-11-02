def solution():
    """Jean has 30 lollipops. Jean eats 2 of the lollipops. With the remaining lollipops, Jean wants to package 2 lollipops in one bag. How many bags can Jean fill?"""
    total_lollipops = 30
    eaten_lollipops = 2
    remaining_lollipops = total_lollipops - eaten_lollipops
    lollipops_per_bag = 2
    bags_filled = remaining_lollipops // lollipops_per_bag
    result = bags_filled
    return result

print(solution())