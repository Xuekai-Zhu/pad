def solution():
    """Nathan wants to line the inside of a box with velvet. The box has two long sides that measure 8 inches by 6 inches, two short sides that measure 5 inches by six inches and a top and a bottom that each measure 40 square inches. How many square inches of velvet does Nathan need?"""
    long_side_area = 8 * 6 * 2
    short_side_area = 5 * 6 * 2
    top_bottom_area = 40 * 2
    total_area = long_side_area + short_side_area + top_bottom_area
    result = total_area
    return result

print(solution())