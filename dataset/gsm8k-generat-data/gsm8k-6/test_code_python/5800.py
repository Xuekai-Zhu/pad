def solution():
    # Calculate the number of drawings Anne can make with her markers
    total_drawings = 12 * 1.5  # each marker lasts for about 1.5 drawings
    remaining_drawings = total_drawings - 8  # Anne has already made 8 drawings
    result = remaining_drawings
    return result

print(solution())