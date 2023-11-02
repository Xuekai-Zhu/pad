def solution():
    num_stickers = 135
    used_stickers = num_stickers / 3
    remaining_stickers = num_stickers - used_stickers
    given_away_stickers = (2 / 5) * remaining_stickers
    stickers_kept = remaining_stickers - given_away_stickers
    result = stickers_kept
    return result

print(solution())