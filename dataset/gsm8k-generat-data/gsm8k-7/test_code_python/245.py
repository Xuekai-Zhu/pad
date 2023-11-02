def solution():
    num_crates = 12
    oranges_per_crate = 150

    num_boxes = 16
    nectarines_per_box = 30

    # Calculate the total number of oranges in all crates
    total_oranges = num_crates * oranges_per_crate

    # Calculate the total number of nectarines in all boxes
    total_nectarines = num_boxes * nectarines_per_box

    # Calculate the total number of fruit pieces
    total_fruit = total_oranges + total_nectarines
    result = total_fruit
    return result

print(solution())