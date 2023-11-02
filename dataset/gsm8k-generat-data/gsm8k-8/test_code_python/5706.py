def solution():
    # Define the number of folders and the number of sheets of paper in each folder
    num_folders = 3
    num_sheets_per_folder = 10

    # Calculate the total number of sheets of paper
    total_num_sheets = num_folders * num_sheets_per_folder

    # Calculate the total number of stickers used
    total_num_stickers = 3 * 10 + 2 * 10 + 1 * 10

    result = total_num_stickers
    return result

print(solution())