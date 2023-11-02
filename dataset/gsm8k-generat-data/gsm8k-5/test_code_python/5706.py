def solution():
    folders = 3  # Peggy buys 3 folders
    sheets_per_folder = 10  # She puts 10 sheets of paper in each folder

    # Calculate the number of stickers in the red folder
    stickers_in_red = sheets_per_folder * 3

    # Calculate the number of stickers in the green folder
    stickers_in_green = sheets_per_folder * 2

    # Calculate the number of stickers in the blue folder
    stickers_in_blue = sheets_per_folder * 1

    # Calculate the total number of stickers Peggy uses
    total_stickers = (stickers_in_red + stickers_in_green + stickers_in_blue) * folders
    result = total_stickers
    return result

print(solution())