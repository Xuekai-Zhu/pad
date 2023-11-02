def solution():
    total_drawings = 25
    colored_pencil_drawings = 14
    blending_marker_drawings = 7

    # Calculate the total number of charcoal drawings
    charcoal_drawings = total_drawings - colored_pencil_drawings - blending_marker_drawings
    result = charcoal_drawings
    return result

print(solution())