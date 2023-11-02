def solution():
    """There are forty apples in one box. Uncle Franky ordered two boxes of apples. He is planning to pack the apples with eight apples in one pack. How many packs of apples can he make with the two boxes of apples?"""
    apples_per_box = 40
    num_boxes = 2
    apples_per_pack = 8
    total_apples = apples_per_box * num_boxes
    packs = total_apples // apples_per_pack
    result = packs
    return result

print(solution())