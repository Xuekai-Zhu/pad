def solution():
    num_eggs = 12
    weight_per_egg = 10
    num_boxes = 4

    # Calculate the total weight of all eggs
    total_weight = num_eggs * weight_per_egg

    # Calculate the total weight of eggs in each box
    weight_per_box = total_weight / num_boxes

    # Calculate the weight of the remaining eggs
    remaining_weight = total_weight - weight_per_box

    result = remaining_weight
    return result

print(solution())