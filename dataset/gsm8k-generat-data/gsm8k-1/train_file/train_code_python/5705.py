def solution():
    """Peggy buys 3 folders, one each in the colors red, green, and blue. She puts ten sheets of paper in each folder, and then, she puts star-shaped stickers on each sheet of paper. In the red folder, each sheet of paper gets 3 stickers. In the green folder, each sheet of paper gets 2 stickers, and in the blue folder, each sheet gets 1 sticker. What is the total number of stickers Peggy uses?"""
    folders = 3
    sheets_per_folder = 10
    red_stickers_per_sheet = 3
    green_stickers_per_sheet = 2
    blue_stickers_per_sheet = 1
    
    total_red_stickers = folders * sheets_per_folder * red_stickers_per_sheet
    total_green_stickers = folders * sheets_per_folder * green_stickers_per_sheet
    total_blue_stickers = folders * sheets_per_folder * blue_stickers_per_sheet
    
    total_stickers = total_red_stickers + total_green_stickers + total_blue_stickers
    result = total_stickers
    return result

print(solution())