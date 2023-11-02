def solution():
    num_markers = 12
    markers_per_drawing = 1.5
    num_drawings = 8

    # Calculate the total number of drawings Anne can make before she runs out of markers
    total_markings = num_markers * markers_per_drawing
    remaining_markings = total_markings - (num_drawings * markers_per_drawing)
    num_remaining_drawings = remaining_markings / markers_per_drawing
    result = num_remaining_drawings
    return result

print(solution())