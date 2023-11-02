def solution():
    
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