def solution():
    total_height = 60
    legs_height = total_height / 3
    head_height = total_height / 4
    rest_of_body_height = total_height - legs_height - head_height

    result = rest_of_body_height
    return result

print(solution())