def solution():
    """Lucille made an agreement with her mom that she would earn six cents for every weed she pulled in her mom's garden. There are eleven weeds in the flower bed, fourteen in the vegetable patch, and thirty-two in the grass around the fruit trees. Lucille weeded the flower bed, the vegetable patch, and half the grass before she took a break. She bought a soda for 99 cents on her break with some of her earnings. How many cents does Lucille have left?"""
    flower_bed_weeds = 11
    vegetable_patch_weeds = 14
    grass_weeds = 32
    total_weeds = flower_bed_weeds + vegetable_patch_weeds + grass_weeds
    half_grass_weeds = grass_weeds / 2
    total_weeds_weeded = flower_bed_weeds + vegetable_patch_weeds + half_grass_weeds
    earnings = total_weeds_weeded * 6
    remaining_earnings = earnings - 99
    result = remaining_earnings
    return result

print(solution())