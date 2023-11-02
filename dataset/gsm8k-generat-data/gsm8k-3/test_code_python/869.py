def solution():
    """Paige bought some new stickers and wanted to share them with 3 of her friends. She decided to share a sheet of 100 space stickers and a sheet of 50 cat stickers equally among her 3 friends. How many stickers will she have left?"""
    # Define the number of stickers on each sheet and the number of friends
    SPACE_STICKERS = 100
    CAT_STICKERS = 50
    NUM_FRIENDS = 3

    # Calculate the number of stickers each friend will receive
    space_per_friend = SPACE_STICKERS // NUM_FRIENDS
    cat_per_friend = CAT_STICKERS // NUM_FRIENDS

    # Calculate the total number of stickers that will be given away
    total_given = (space_per_friend + cat_per_friend) * NUM_FRIENDS

    # Calculate the number of stickers left over
    total_stickers = SPACE_STICKERS + CAT_STICKERS
    left_over = total_stickers - total_given

    # Display the number of stickers left over
    result = left_over
    return result

print(solution())