def solution():
    
    crates = 10
    boxes_per_crate = 6
    machines_per_box = 4
    machines_removed_per_box = 1
    total_boxes = crates * boxes_per_crate
    total_machines = total_boxes * machines_per_box
    machines_removed = total_boxes * machines_removed_per_box
    result = machines_removed
    return result

print(solution())