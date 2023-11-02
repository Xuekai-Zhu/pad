def solution():
    """Paige bought some new stickers and wanted to share them with 3 of her friends. She decided to share a sheet of 100 space stickers and a sheet of 50 cat stickers equally among her 3 friends. How many stickers will she have left?"""
    # Define the number of friends
    num_friends = 3

    # Define the number of space stickers and cat stickers
    space_stickers = 100
    cat_stickers = 50

    # Calculate the total number of stickers
    total_stickers = space_stickers + cat_stickers

    # Divide the stickers equally among the friends and calculate the number of stickers left
    stickers_left = total_stickers % num_friends

    # return the result
    result = stickers_left
    return result

print(solution())