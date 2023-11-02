def solution():
    num_packs = 2
    num_sheets_per_pack = 240
    num_pages_per_day = 80

    # Calculate the total number of sheets of paper purchased
    total_num_sheets = num_packs * num_sheets_per_pack

    # Calculate the total number of days the paper will last
    total_num_days = total_num_sheets / (num_pages_per_day * 1.0)
    result = total_num_days
    return result

print(solution())