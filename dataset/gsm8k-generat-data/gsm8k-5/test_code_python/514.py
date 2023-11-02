def solution():
    initial_stickers = 100  # Clara starts with 100 stickers
    given_to_crush = 10  # Clara gives 10 stickers to the boy she likes
    remaining_stickers = initial_stickers - given_to_crush  # Clara has this many stickers left

    # Clara gives half of the remaining stickers to her best friends
    given_to_friends = remaining_stickers / 2
    remaining_stickers -= given_to_friends

    result = remaining_stickers
    return result

print(solution())