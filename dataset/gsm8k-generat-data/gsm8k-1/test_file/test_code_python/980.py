def solution():
    """Pat has a flower bed that is 111 feet long. Pat wants to fill her flower bed with plants. Pat's flowers grow 12 inches wide so she needs to leave 1.5 feet between every plant. Pat already owns 17 flowers. Each flowering plant costs $6 at the store, how much money will Pat spend at the store to fill up her flower bed?"""
    flower_bed_length = 111
    plant_width = 1  # in feet
    space_between_plants = 1.5  # in feet
    total_space_needed = flower_bed_length * 2 + 1  # to cover both sides of the flower bed
    space_for_plants = total_space_needed - plant_width * 17 - space_between_plants * 16  # subtracting the space taken up by existing plants and the space between plants
    plants_needed = space_for_plants / (plant_width + space_between_plants)
    cost_per_plant = 6
    total_cost = plants_needed * cost_per_plant
    result = total_cost
    return result

print(solution())