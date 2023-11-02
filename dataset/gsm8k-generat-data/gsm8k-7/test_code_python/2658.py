def solution():
    total_stickers = 100
    andrew_share = total_stickers * 1 / 5
    remaining_stickers = total_stickers - andrew_share
    bill_share = remaining_stickers * 3 / 10
    andrew_gives = andrew_share / 2
    result = andrew_gives
    return result

print(solution())