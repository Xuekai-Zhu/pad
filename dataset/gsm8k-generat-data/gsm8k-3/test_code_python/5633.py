def solution():
    """Thomas has 25 drawings to display. 14 of the drawings were made using colored pencils. 7 of the drawings were made using blending markers. The rest of the drawings were made with charcoal. How many are charcoal drawings?"""
    # Define the number of colored pencil and blending marker drawings
    colored_pencil_drawings = 14
    blending_marker_drawings = 7

    # Calculate the number of charcoal drawings
    charcoal_drawings = 25 - colored_pencil_drawings - blending_marker_drawings

    # Display the number of charcoal drawings
    result = charcoal_drawings
    return result

print(solution())