def solution():
    """Zander collected 100 stickers. He gave some of his stickers to his two friends, Andrew and Bill. Andrew received 1/5 of Zander's stickers, while Bill received 3/10 of the remaining stickers. How many stickers did Andrew give to his two friends?"""
    zander_stickers = 100
    andrew_share = zander_stickers / 5
    remaining_stickers = zander_stickers - andrew_share
    bill_share = remaining_stickers * (3/10)
    andrew_gave_to_bill = bill_share / 2
    result = andrew_gave_to_bill
    return result

print(solution())