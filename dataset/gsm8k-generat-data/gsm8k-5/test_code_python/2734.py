def solution():
    basil_plants = 3
    rosemary_plants = 9
    thyme_plants = 6

    basil_leaves_per_plant = 4
    rosemary_leaves_per_plant = 18
    thyme_leaves_per_plant = 30

    total_basil_leaves = basil_plants * basil_leaves_per_plant
    total_rosemary_leaves = rosemary_plants * rosemary_leaves_per_plant
    total_thyme_leaves = thyme_plants * thyme_leaves_per_plant

    total_leaves = total_basil_leaves + total_rosemary_leaves + total_thyme_leaves
    result = total_leaves
    return result

print(solution())