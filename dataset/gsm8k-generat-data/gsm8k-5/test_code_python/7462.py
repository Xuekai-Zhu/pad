def solution():
    initial_bars = 100  # Steve finds 100 gold bars
    friends = 4  # Steve wants to distribute the bars evenly among 4 friends
    lost_bars = 20  # 20 gold bars were lost on the way back to San Diego

    # Calculate the total number of gold bars after accounting for lost bars
    total_bars = initial_bars - lost_bars

    # Calculate the number of gold bars each friend will get
    bars_per_friend = total_bars // friends
    result = bars_per_friend
    return result

print(solution())