def solution():
    total_markers = 12
    drawings_per_marker = 1.5
    drawings_made = 8
    drawings_left = total_markers * drawings_per_marker - drawings_made
    result = drawings_left
    return result

print(solution())