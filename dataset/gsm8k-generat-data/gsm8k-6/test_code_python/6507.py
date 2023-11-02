def solution():
    # Calculate the number of sheets of paper in one binder
    num_sheets_per_binder = 2450/5

    # Calculate the number of sheets of paper Justine colored on
    num_colored_sheets = num_sheets_per_binder/2

    result = num_colored_sheets
    return result

print(solution())