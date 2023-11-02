def solution():
    # Convert map distance to actual distance
    map_to_actual = 8 / 0.25  # 1/4 inch represents 8 miles

    # Calculate actual distance between Pence and Hillcrest
    distance = map_to_actual * 3.375  # 3 3/8 inches apart on the map

    result = distance
    return result

print(solution())