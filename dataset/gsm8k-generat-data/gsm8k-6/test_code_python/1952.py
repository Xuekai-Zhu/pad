def solution():
    # Calculate the total number of candy bars sold by Sol in a week
    total_candy_bars = 10 + 14 + 18 + 22 + 26 + 30  # Sol sells 10 candy bars on the first day and 4 more than the previous day each day after that
    # Calculate the total earnings from selling candy bars in a week
    total_earnings = total_candy_bars * 0.10  # each candy bar costs 10 cents
    result = total_earnings
    return result

print(solution())