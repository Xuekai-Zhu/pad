def solution():
    """Anne is drawing pictures. She has 12 markers and she notices that each one lasts for about 1.5 drawings. If she has already made 8 drawings, how many more can she make before she runs out of markers?"""
    markers = 12
    markers_per_drawing = 1.5
    drawings_done = 8
    total_drawings_possible = markers * markers_per_drawing
    remaining_drawings_possible = total_drawings_possible - (drawings_done * markers_per_drawing)
    result = remaining_drawings_possible
    return result

print(solution())