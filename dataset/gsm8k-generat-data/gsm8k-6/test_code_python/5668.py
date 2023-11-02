def solution():
    # Calculate the total number of sheets of paper in the two packs
    total_sheets = 2 * 240

    # Calculate the number of days the paper will last
    days_last = total_sheets // 80  # integer division gives the number of whole days
    result = days_last
    return result

print(solution())