def solution():
    sheets_left = 5  # Xia had five sheets of stickers left
    stickers_per_sheet = 10  # Each sheet had ten stickers on it
    total_stickers = 100 + (sheets_left * stickers_per_sheet)  # Xia shared 100 stickers with her friends and had five left
    stickers_at_beginning = total_stickers - (sheets_left * stickers_per_sheet)  # Subtract the stickers on the five sheets Xia had left
    result = stickers_at_beginning
    return result

print(solution())