def solution():
    space_stickers_per_friend = 100 // 3  # Paige shares a sheet of 100 space stickers equally among 3 friends
    cat_stickers_per_friend = 50 // 3  # Paige shares a sheet of 50 cat stickers equally among 3 friends

    # Calculate the total number of stickers shared among the 3 friends
    total_shared_stickers = (space_stickers_per_friend + cat_stickers_per_friend) * 3

    # Calculate the number of stickers left after sharing
    total_stickers = 100 + 50  # Paige had 100 space stickers and 50 cat stickers
    stickers_left = total_stickers - total_shared_stickers
    result = stickers_left
    return result

print(solution())