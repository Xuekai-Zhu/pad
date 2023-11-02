def solution():
    """Marie, the confectioner, makes 12 chocolate eggs, each weighing 10 ounces. She then packs an equal number of the eggs in 4 different gift boxes. Unfortunately, she leaves one of the boxes by the kitchen window and the afternoon sun melts everything. She tosses that box out. What is the total weight, in ounces, of the remaining chocolate eggs?"""
    num_boxes = 4
    num_eggs_per_box = 12 // num_boxes
    remaining_eggs = 12 - num_eggs_per_box
    remaining_weight = remaining_eggs * 10
    result = remaining_weight
    return result

print(solution())