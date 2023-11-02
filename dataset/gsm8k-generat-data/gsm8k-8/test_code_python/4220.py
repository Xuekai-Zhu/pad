def solution():
    # Define the number of packs and sticks of gum per carton
    packs_per_carton = 5
    sticks_per_pack = 3

    # Calculate the total number of sticks of gum per carton
    gum_per_carton = packs_per_carton * sticks_per_pack

    # Calculate the total number of sticks of gum per brown box
    gum_per_box = gum_per_carton * 4

    # Calculate the total number of sticks of gum in 8 brown boxes
    total_gum = gum_per_box * 8
    result = total_gum
    return result

print(solution())