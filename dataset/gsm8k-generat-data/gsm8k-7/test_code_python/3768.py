def solution():
    num_crates = 10
    boxes_per_crate = 6
    machines_per_box = 4
    machines_removed_per_box = 1

    # Calculate the total number of boxes in the container
    total_boxes = num_crates * boxes_per_crate

    # Calculate the total number of machines in the container before removal
    total_machines_before_removal = total_boxes * machines_per_box

    # Calculate the total number of machines removed
    total_machines_removed = total_boxes * machines_removed_per_box

    result = total_machines_removed
    return result

print(solution())