def solution():
    """After sharing 100 stickers with her friends, Xia had five sheets of stickers left. If each sheet had ten stickers on it, how many stickers did Xia have at the beginning?"""
    leftover_sheets = 5
    stickers_per_sheet = 10
    total_leftover_stickers = leftover_sheets * stickers_per_sheet
    total_stickers_at_beginning = total_leftover_stickers + 100
    result = total_stickers_at_beginning
    return result

print(solution())