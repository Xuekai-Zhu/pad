def solution():
    """There are 160 tissues inside a tissue box.   If Tucker bought 3 boxes, and used 210 tissues while he was sick with the flu, how many tissues would he have left?"""
    tissues_per_box = 160
    num_boxes = 3
    total_tissues = tissues_per_box * num_boxes
    used_tissues = 210
    remaining_tissues = total_tissues - used_tissues
    result = remaining_tissues
    return result

print(solution())