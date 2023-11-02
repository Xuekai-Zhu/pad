def solution():
    total_singers = 30
    first_group = total_singers / 2
    second_group = (total_singers - first_group) / 3
    third_group = total_singers - first_group - second_group
    result = third_group
    return result

print(solution())