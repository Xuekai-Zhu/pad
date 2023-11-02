def solution():
    num_sheets_left = 5
    num_stickers_per_sheet = 10
    total_stickers_shared = 100

    # Calculate the total number of stickers Xia had at the end
    num_stickers_left = num_sheets_left * num_stickers_per_sheet
    total_stickers_end = num_stickers_left + total_stickers_shared

    # Calculate the number of stickers Xia had at the beginning
    num_stickers_start = total_stickers_end - total_stickers_shared
    result = num_stickers_start
    return result

print(solution())