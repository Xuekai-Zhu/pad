def solution():
    # Calculate the total number of sticks of gum in 8 brown boxes
    packs_per_carton = 5
    sticks_per_pack = 3
    sticks_per_carton = packs_per_carton * sticks_per_pack
    cartons_per_box = 4
    sticks_per_box = sticks_per_carton * cartons_per_box
    total_sticks = sticks_per_box * 8
    result = total_sticks
    return result

print(solution())