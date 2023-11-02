def solution():
    total_students = 30
    num_girls = 18
    num_green = total_students // 2
    num_pink = num_girls // 3
    num_yellow = total_students - num_green - num_pink
    result = num_yellow
    return result

print(solution())