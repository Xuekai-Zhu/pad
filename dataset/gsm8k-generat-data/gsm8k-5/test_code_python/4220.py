def solution():
    # Calculate the number of sticks of gum per carton and per brown box
    sticks_per_pack = 3
    packs_per_carton = 5
    sticks_per_carton = sticks_per_pack * packs_per_carton
    cartons_per_brown_box = 4

    # Calculate the total number of sticks of gum in 8 brown boxes
    total_cartons = 8 * cartons_per_brown_box
    total_sticks = total_cartons * sticks_per_carton
    result = total_sticks
    return result

print(solution())