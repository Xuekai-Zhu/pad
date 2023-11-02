def solution():
    
    clothes_wash_time = 30
    towels_wash_time = clothes_wash_time * 2
    sheets_wash_time = towels_wash_time - 15
    total_wash_time = clothes_wash_time + towels_wash_time + sheets_wash_time
    result = total_wash_time
    return result

print(solution())