def solution():
    """After sharing 100 stickers with her friends, Xia had five sheets of stickers left. If each sheet had ten stickers on it, how many stickers did Xia have at the beginning?"""
    # Define the number of stickers on each sheet
    STICKERS_PER_SHEET = 10

    # Calculate the total number of stickers Xia had at the end
    total_stickers = 5 * STICKERS_PER_SHEET + 100

    # Calculate the number of stickers Xia had at the beginning
    initial_stickers = total_stickers - 5 * STICKERS_PER_SHEET

    # Display the number of stickers Xia had at the beginning
    result = initial_stickers
    return result

print(solution())