def solution():
    shed_width = 3
    shed_length = 5
    backyard_width = 20
    backyard_length = 13
    shed_area = shed_width * shed_length
    backyard_area = backyard_width * backyard_length
    total_area = backyard_area - shed_area
    result = total_area
    return result

print(solution())