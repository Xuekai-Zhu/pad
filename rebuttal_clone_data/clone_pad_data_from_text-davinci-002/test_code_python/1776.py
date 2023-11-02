def solution():
    class_size = 30
    required_average = 75
    current_average = 74
    points_needed = (required_average * class_size) - (current_average * (class_size - 1))
    result = points_needed
    return result

print(solution())