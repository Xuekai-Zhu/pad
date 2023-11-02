def solution():
    """Peggy buys 3 folders, one each in the colors red, green, and blue.  She puts ten sheets of paper in each folder, and then, she puts star-shaped stickers on each sheet of paper.  In the red folder, each sheet of paper gets 3 stickers.  In the green folder, each sheet of paper gets 2 stickers, and in the blue folder, each sheet gets 1 sticker.  What is the total number of stickers Peggy uses?"""
    # Define the number of sheets of paper per folder
    SHEETS_PER_FOLDER = 10

    # Define the number of stickers per sheet of paper for each folder
    RED_STICKERS = 3
    GREEN_STICKERS = 2
    BLUE_STICKERS = 1

    # Calculate the total number of stickers used
    total_stickers = (SHEETS_PER_FOLDER * RED_STICKERS) + (SHEETS_PER_FOLDER * GREEN_STICKERS) + (SHEETS_PER_FOLDER * BLUE_STICKERS)

    # Display the total number of stickers
    result = total_stickers
    return result

print(solution())