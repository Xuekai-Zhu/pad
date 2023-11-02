def solution():
    # Calculate the total number of records Jerry has
    total_records = 4 * 3 * 20 * 0.6  # 4 cases, 3 shelves per case, each shelf can hold 20 records at 60% capacity
    total_ridges = total_records * 60  # each record has 60 ridges
    result = total_ridges
    return result

print(solution())