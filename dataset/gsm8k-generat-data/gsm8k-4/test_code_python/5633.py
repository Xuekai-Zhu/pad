def solution():
    """Thomas has 25 drawings to display. 14 of the drawings were made using colored pencils. 7 of the drawings were made using blending markers. The rest of the drawings were made with charcoal. How many are charcoal drawings?"""
    # Define the total number of drawings and the number of drawings made with colored pencils and blending markers
    total_drawings = 25
    pencil_drawings = 14
    marker_drawings = 7

    # Calculate the number of drawings made with charcoal
    charcoal_drawings = total_drawings - pencil_drawings - marker_drawings

    # Return the result
    result = charcoal_drawings
    return result

print(solution())