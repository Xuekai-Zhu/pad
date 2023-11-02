def solution():
    """There are 12 crates that each contain 150 oranges. There are 16 boxes that each hold 30 nectarines. How many pieces of fruit are in the crates and the boxes in total?"""
    crates = 12
    oranges_per_crate = 150
    boxes = 16
    nectarines_per_box = 30
    total_oranges = crates * oranges_per_crate
    total_nectarines = boxes * nectarines_per_box
    total_fruit = total_oranges + total_nectarines
    result = total_fruit
    return result

print(solution())