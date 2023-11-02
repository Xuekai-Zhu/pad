def solution():
    """Peggy buys 3 folders, one each in the colors red, green, and blue. She puts ten sheets of paper in each folder, and then, she puts star-shaped stickers on each sheet of paper. In the red folder, each sheet of paper gets 3 stickers. In the green folder, each sheet of paper gets 2 stickers, and in the blue folder, each sheet gets 1 sticker. What is the total number of stickers Peggy uses?"""
    # Define the number of folders and sheets of paper in each folder
    num_folders = 3
    sheets_per_folder = 10

    # Define the number of stickers for each sheet of paper in each folder
    red_stickers_per_sheet = 3
    green_stickers_per_sheet = 2
    blue_stickers_per_sheet = 1

    # Calculate the total number of stickers used
    total_stickers = (red_stickers_per_sheet * sheets_per_folder) + (green_stickers_per_sheet * sheets_per_folder) + (blue_stickers_per_sheet * sheets_per_folder)

    # Display the result
    result = total_stickers
    return result

print(solution())