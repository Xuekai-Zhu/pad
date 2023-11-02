def solution():
    """Peter has four horses. Each one eats 4 pounds of oats, twice a day, and 3 pounds of grain once a day. How many pounds of food does he need to feed his horses for 3 days?"""
    horses = 4
    oats_per_day = 4 * 2
    grain_per_day = 3
    food_per_day = horses * (oats_per_day + grain_per_day)
    total_food = food_per_day * 3
    result = total_food
    return result

print(solution())