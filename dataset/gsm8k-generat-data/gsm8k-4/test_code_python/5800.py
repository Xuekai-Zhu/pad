def solution():
    """Anne is drawing pictures. She has 12 markers and she notices that each one lasts for about 1.5 drawings. If she has already made 8 drawings, how many more can she make before she runs out of markers?"""
    # Define the number of markers and the efficiency of each marker
    markers = 12
    marker_efficiency = 1.5

    # Calculate the total number of drawings possible
    total_drawings = markers * marker_efficiency

    # Calculate the number of drawings already made
    drawings_made = 8

    # Calculate the number of drawings that can still be made
    drawings_left = total_drawings - drawings_made

    # Return the result
    result = drawings_left
    return result

print(solution())