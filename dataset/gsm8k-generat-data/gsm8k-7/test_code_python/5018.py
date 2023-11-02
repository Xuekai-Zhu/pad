def solution():
    num_boxes_per_carton = 12
    num_packs_per_box = 10
    num_cartons = 12
    total_cost = 1440

    # Calculate the total number of packs of cheese cookies
    total_packs = num_boxes_per_carton * num_packs_per_box * num_cartons

    # Calculate the cost per pack of cheese cookies
    cost_per_pack = total_cost / total_packs
    result = cost_per_pack
    return result

print(solution())