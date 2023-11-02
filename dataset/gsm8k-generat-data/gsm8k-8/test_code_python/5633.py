def solution():
    total_drawings = 25
    colored_drawings = 14
    marker_drawings = 7

    charcoal_drawings = total_drawings - colored_drawings - marker_drawings
    result = charcoal_drawings
    return result

print(solution())