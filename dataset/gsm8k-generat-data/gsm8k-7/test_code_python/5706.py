def solution():
    num_folders = 3
    num_sheets_per_folder = 10

    # Calculate the total number of stickers used in the red folder
    red_stickers_per_sheet = 3
    red_stickers_total = red_stickers_per_sheet * num_sheets_per_folder

    # Calculate the total number of stickers used in the green folder
    green_stickers_per_sheet = 2
    green_stickers_total = green_stickers_per_sheet * num_sheets_per_folder

    # Calculate the total number of stickers used in the blue folder
    blue_stickers_per_sheet = 1
    blue_stickers_total = blue_stickers_per_sheet * num_sheets_per_folder

    # Calculate the total number of stickers used
    total_stickers_used = red_stickers_total + green_stickers_total + blue_stickers_total
    result = total_stickers_used
    return result

print(solution())