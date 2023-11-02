def solution():
    total_drawings = 25  # Thomas has a total of 25 drawings
    colored_pencils = 14  # 14 of the drawings were made using colored pencils
    blending_markers = 7  # 7 of the drawings were made using blending markers

    # Calculate the number of charcoal drawings
    charcoal_drawings = total_drawings - colored_pencils - blending_markers
    result = charcoal_drawings
    return result

print(solution())