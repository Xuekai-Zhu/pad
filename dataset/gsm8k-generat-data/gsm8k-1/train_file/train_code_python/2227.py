def solution():
    """Billy has four horses. Each one eats 4 pounds of oats, twice a day. How many pounds of oats does he need to feed his horses for 3 days?"""
    num_horses = 4
    oats_per_horse_per_day = 4 * 2
    num_days = 3
    total_oats = num_horses * oats_per_horse_per_day * num_days
    result = total_oats
    return result

print(solution())