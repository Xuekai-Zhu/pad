def solution():
    """Zander collected 100 stickers. He gave some of his stickers to his two friends, Andrew and Bill. Andrew received 1/5 of Zander's stickers, while Bill received 3/10 of the remaining stickers. How many stickers did Andrew give to his two friends?"""
    zander_stickers = 100
    andrew_stickers = zander_stickers / 5
    remaining_stickers = zander_stickers - andrew_stickers
    bill_stickers = remaining_stickers * 3 / 10
    andrew_gives = (andrew_stickers - bill_stickers) / 2
    result = andrew_gives
    return result

print(solution())