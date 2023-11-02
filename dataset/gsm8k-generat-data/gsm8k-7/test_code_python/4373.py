def solution():
    weeds_in_flower_bed = 11
    weeds_in_veggie_patch = 14
    weeds_in_fruit_tree_grass = 32

    earnings_per_weed = 6  # cents per weed
    total_weeds_pulled = (weeds_in_flower_bed + weeds_in_veggie_patch + weeds_in_fruit_tree_grass) * 0.5

    total_earnings = earnings_per_weed * total_weeds_pulled

    soda_cost = 99  # cents
    earnings_left = total_earnings - soda_cost
    result = earnings_left
    return result

print(solution())