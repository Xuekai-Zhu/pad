def solution():
    
    flower_bed_length = 111
    flower_width = 12
    flowering_plants_per_plant = 1.5
    flowers_owned = 17
    flowering_plants_needed = flower_bed_length - (flower_width * flowering_plants_per_plant)
    cost_per_flowering_plant = 6
    total_cost = flowering_plants_needed * cost_per_flowering_plant
    result = total_cost
    return result

print(solution())