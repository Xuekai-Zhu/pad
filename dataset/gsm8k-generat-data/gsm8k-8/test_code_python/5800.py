def solution():
    # Define the number of markers and drawings Anne has
    total_markers = 12
    markers_per_drawing = 1.5
    drawings_completed = 8

    # Calculate the total number of markers used so far
    markers_used = markers_per_drawing * drawings_completed

    # Calculate the number of markers remaining
    markers_remaining = total_markers - markers_used

    # Calculate the maximum number of drawings Anne can make before running out of markers
    max_drawings = markers_remaining / markers_per_drawing

    result = max_drawings
    return result

print(solution())