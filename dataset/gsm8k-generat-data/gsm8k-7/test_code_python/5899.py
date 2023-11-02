def solution():
    total_length = 100
    longer_side = 28
    # Calculation of the shorter sides length using perimeter formula of rectangle 2(l+b) =100+28+28 = 156cm
    shorter_sides_length = (156 - 2 * longer_side) / 2
    result = shorter_sides_length
    return result

print(solution())