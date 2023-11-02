def solution():
    sharks = 4
    dolphins = sharks / 2
    other_animals = sharks * 5
    total_animals = sharks + dolphins + other_animals
    total_buckets = 546
    total_weeks = total_buckets / total_animals
    result = total_weeks
    return result

print(solution())