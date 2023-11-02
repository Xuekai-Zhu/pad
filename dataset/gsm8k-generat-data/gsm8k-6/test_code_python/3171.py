def solution():
    # Calculate the total length of tape needed to tape up the boxes
    tape_for_15_by_30 = (15 + 30*2) * 5 * 3  # each box needs one piece as long as the long side and two as long as the short side
    tape_for_40_square = 40 * 4 * 2  # square box has all sides of equal length, so one piece for each side and two for the smaller sides
    total_tape = tape_for_15_by_30 + tape_for_40_square
    result = total_tape
    return result

print(solution())