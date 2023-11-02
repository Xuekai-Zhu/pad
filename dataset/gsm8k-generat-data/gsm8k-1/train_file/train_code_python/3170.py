def solution():
    """Brian is taping up some boxes. Each box needs three pieces of tape, one as long as the long side and two as long as the short side. If Brian tapes up 5 boxes that measure 15 inches by 30 inches and 2 boxes that measure 40 inches square, how much tape does he need?"""
    boxes_15_30 = 5
    boxes_40 = 2
    tape_length_15_30 = 15 + (2 * 30)  # long side + 2 short sides
    tape_length_40 = 2 * 40  # 2 short sides (all sides are equal)
    total_tape = (boxes_15_30 * tape_length_15_30 + boxes_40 * tape_length_40) * 3  # each box needs 3 pieces of tape
    result = total_tape
    return result

print(solution())