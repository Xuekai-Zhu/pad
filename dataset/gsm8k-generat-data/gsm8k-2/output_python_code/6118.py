def solution():
    """Peter has four horses. Each one eats 4 pounds of oats, twice a day, and 3 pounds of grain once a day. 
    How many pounds of food does he need to feed his horses for 3 days?"""
    num_horses = 4
    oats_per_day = 4 * 2 + 3
    oats_per_three_days = oats_per_day * 3
    total_oats = oats_per_three_days * num_horses
    result = total_oats
    return result

print(solution())