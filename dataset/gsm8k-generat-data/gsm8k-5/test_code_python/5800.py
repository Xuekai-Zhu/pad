def solution():
    markers_per_drawing = 1.5  # Each marker lasts for 1.5 drawings
    total_markers = 12  # Anne has 12 markers
    used_markers = (markers_per_drawing * 8)  # Anne has already used markers for 8 drawings

    # Calculate the number of drawings Anne can make with the remaining markers
    remaining_markers = total_markers - used_markers
    remaining_drawings = remaining_markers / markers_per_drawing
    result = remaining_drawings
    return result

print(solution())