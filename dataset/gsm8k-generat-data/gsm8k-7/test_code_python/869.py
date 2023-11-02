def solution():
    num_friends = 3
    space_stickers_per_sheet = 100
    cat_stickers_per_sheet = 50

    # Calculate the total number of stickers on the space sticker sheet
    total_space_stickers = space_stickers_per_sheet

    # Calculate the total number of stickers on the cat sticker sheet
    total_cat_stickers = cat_stickers_per_sheet

    # Calculate the total number of stickers Paige will give away
    total_given_stickers = (total_space_stickers + total_cat_stickers) / num_friends

    # Calculate the number of stickers Paige will have left
    num_stickers_left = (total_space_stickers + total_cat_stickers) - (total_given_stickers * num_friends)
    result = num_stickers_left
    return result

print(solution())