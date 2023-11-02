def solution():
    initial_elevation = 100
    final_elevation = 1450
    vertical_distance = final_elevation - initial_elevation

    # For every 1 foot vertical, John travels 2 feet horizontally
    horizontal_distance = vertical_distance * 2
    result = horizontal_distance
    return result

print(solution())