def solution():
    # Calculate the area of the largest room
    largest_width = 45
    largest_length = 30
    largest_area = largest_width * largest_length

    # Calculate the area of the smallest room
    smallest_width = 15
    smallest_length = 8
    smallest_area = smallest_width * smallest_length

    # Calculate the difference in area between the largest and smallest rooms
    area_difference = largest_area - smallest_area
    result = area_difference
    return result

print(solution())