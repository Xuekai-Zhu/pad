def solution():
    """Billy has four horses. Each one eats 4 pounds of oats, twice a day. How many pounds of oats does he need to feed his horses for 3 days?"""
    horses = 4
    oats_per_day = 4 * 2
    days = 3
    total_oats = horses * oats_per_day * days
    result = total_oats
    return result

print(solution())