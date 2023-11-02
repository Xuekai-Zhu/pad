def solution():
    """Brian is taping up some boxes. Each box needs three pieces of tape, one as long as the long side and two as long as the short side. If Brian tapes up 5 boxes that measure 15 inches by 30 inches and 2 boxes that measure 40 inches square, how much tape does he need?"""
    tape_per_small_box = 2 * 15 + 30
    tape_per_big_box = 2 * 40 + 40
    total_tape = 5 * tape_per_small_box + 2 * tape_per_big_box
    result = total_tape
    return result

print(solution())