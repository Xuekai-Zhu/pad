def solution():
    # Calculate how many gold bars Steve has after losing 20
    total_gold_bars = 100 - 20

    # Calculate how many gold bars each friend will get
    bars_per_friend = total_gold_bars // 4
    result = bars_per_friend
    return result

print(solution())