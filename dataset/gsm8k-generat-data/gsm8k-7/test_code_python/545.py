def solution():
    num_plants = 3
    num_green_leaves_per_plant = 18
    fraction_yellow_leaves_per_plant = 1/3

    # Calculate the total number of green leaves on all tea leaf plants
    total_green_leaves = num_plants * num_green_leaves_per_plant

    # Calculate the number of yellow leaves that fall off of one tea leaf plant
    num_yellow_leaves_per_plant = fraction_yellow_leaves_per_plant * num_green_leaves_per_plant

    # Calculate the total number of yellow leaves that fall off of all tea leaf plants
    total_yellow_leaves = num_plants * num_yellow_leaves_per_plant

    # Calculate the number of green leaves left on all tea leaf plants
    num_green_leaves_left = total_green_leaves - total_yellow_leaves
    result = num_green_leaves_left
    return result

print(solution())