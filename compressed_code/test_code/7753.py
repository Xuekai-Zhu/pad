def solution():
    
    row1_initial = 24
    row1_missing = 3
    row2_initial = 20
    row2_missing = 5
    row3_initial = 18
    total_relaxing = row1_initial + row2_initial + row3_initial
    total_missing = row1_missing + row2_missing
    remaining_relaxing = total_relaxing - total_missing
    result = remaining_relaxing
    return result

print(solution())