def solution():
    """Sol sells candy bars to raise money for her softball team. On the first day, she sells ten candy bars and sells four more candy bars than she sold the previous day each day afterward. If she sells six days a week and each candy bar costs 10 cents, how much will she earn in a week in dollars?"""
    candy_bars_per_day = [10]  # starting with 10 candy bars on the first day
    for i in range(1, 6):
        candy_bars_per_day.append(candy_bars_per_day[i-1] + 4)  # adding 4 more candy bars each day
    total_candy_bars = sum(candy_bars_per_day)
    total_dollars = total_candy_bars * 0.1  # each candy bar costs 10 cents
    result = total_dollars
    return result

print(solution())