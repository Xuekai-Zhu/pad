def solution():
    # Calculate the number of gold bars Steve has left after losing some on the way
    remaining_bars = 100 - 20

    # Calculate the number of gold bars each friend will get
    bars_per_friend = remaining_bars // 4  # Use integer division to ensure even distribution
    result = bars_per_friend
    return result

print(solution())