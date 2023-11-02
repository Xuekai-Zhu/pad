def solution():
    apples_per_box = 40  # There are 40 apples in one box
    boxes_ordered = 2  # Uncle Franky ordered two boxes of apples
    apples_per_pack = 8  # Uncle Franky is planning to pack the apples with 8 apples in one pack

    # Calculate the total number of apples Uncle Franky can make
    total_apples = apples_ordered * boxes_ordered

    # Calculate the number of packs of apples Uncle Franky can make
    packs_of_apples = total_apples // apples_per_pack
    result = packs_of_apples
    return result

print(solution())