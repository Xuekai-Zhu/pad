def solution():
    """Thomas has 25 drawings to display. 14 of the drawings were made using colored pencils. 7 of the drawings were made using blending markers. The rest of the drawings were made with charcoal. How many are charcoal drawings?"""
    total_drawings = 25
    colored_pencil_drawings = 14
    blending_marker_drawings = 7
    charcoal_drawings = total_drawings - colored_pencil_drawings - blending_marker_drawings
    result = charcoal_drawings
    return result

print(solution())