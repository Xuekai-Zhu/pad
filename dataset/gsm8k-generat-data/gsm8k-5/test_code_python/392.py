def solution():
    clothes_time = 30
    towels_time = clothes_time * 2
    sheets_time = towels_time - 15
    total_time = clothes_time + towels_time + sheets_time
    result = total_time
    return result

print(solution())