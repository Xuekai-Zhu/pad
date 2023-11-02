def solution():
    clothes_time = 30  # time to wash clothes in minutes
    towels_time = clothes_time * 2  # time to wash towels is twice that of clothes
    sheets_time = towels_time - 15  # time to wash sheets is 15 minutes less than time for towels
    total_time = clothes_time + towels_time + sheets_time  # total time to wash everything
    result = total_time
    return result

print(solution())