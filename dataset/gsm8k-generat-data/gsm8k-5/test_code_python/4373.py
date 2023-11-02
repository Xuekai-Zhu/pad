def solution():
    weeds_flower_bed = 11  # There are 11 weeds in the flower bed
    weeds_vegetable_patch = 14  # There are 14 weeds in the vegetable patch
    weeds_grass_fruit_trees = 32  # There are 32 weeds in the grass around the fruit trees
    total_weeds = weeds_flower_bed + weeds_vegetable_patch + weeds_grass_fruit_trees  # Total number of weeds
    earnings_per_weed = 6  # Lucille earns 6 cents per weed
    total_earnings = earnings_per_weed * (weeds_flower_bed + weeds_vegetable_patch + weeds_grass_fruit_trees / 2)  # Lucille's total earnings before buying a soda
    remaining_earnings = total_earnings - 99  # Lucille bought a soda for 99 cents, so this is how much she has left
    result = remaining_earnings
    return result

print(solution())