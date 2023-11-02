def solution():
    """Anne is drawing pictures. She has 12 markers and she notices that each one lasts for about 1.5 drawings. If she has already made 8 drawings, how many more can she make before she runs out of markers?"""
    markers = 12
    drawings_per_marker = 1.5
    drawings_completed = 8
    markers_remaining = markers - (drawings_completed / drawings_per_marker)
    remaining_drawings = markers_remaining * drawings_per_marker
    result = remaining_drawings
    return result

print(solution())