def solution():
    packs_per_carton = 5
    gum_per_pack = 3
    gum_per_carton = packs_per_carton * gum_per_pack
    cartons_per_box = 4
    num_boxes = 8

    # Calculate the total number of cartons of gum in all boxes
    total_cartons = cartons_per_box * num_boxes

    # Calculate the total number of sticks of gum in all cartons
    total_gum = total_cartons * gum_per_carton
    result = total_gum
    return result

print(solution())