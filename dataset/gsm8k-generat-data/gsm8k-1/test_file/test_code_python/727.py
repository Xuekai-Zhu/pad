def solution():
    """Each sleeve of graham crackers makes the base for 8 large smores. There are 3 sleeves in a box. If 9 kids want 2 smores apiece and 6 adults will eat 1 smore apiece, how many boxes of graham crackers will they need?"""
    smores_per_sleeve = 8
    sleeves_per_box = 3
    total_smores = (9 * 2) + (6 * 1)
    boxes_of_graham_crackers = total_smores // smores_per_sleeve // sleeves_per_box + 1
    result = boxes_of_graham_crackers
    return result

print(solution())