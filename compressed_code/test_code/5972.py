def solution():
    
    oranges_per_crate = 150
    crates = 12
    nectarines_per_box = 30
    boxes = 16
    total_oranges = oranges_per_crate * crates
    total_nectarines = nectarines_per_box * boxes
    total_fruit = total_oranges + total_nectarines
    result = total_fruit
    return result

print(solution())