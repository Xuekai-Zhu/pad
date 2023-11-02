def solution():
    """Steve finds 100 gold bars while visiting Oregon. He wants to distribute his gold bars evenly to his 4 friends.
    If 20 gold bars were lost on the way back to San Diego, how many gold bars will each of his 4 friends get when he returns?"""
    total_bars = 100
    lost_bars = 20
    remaining_bars = total_bars - lost_bars
    friends = 4
    bars_each = remaining_bars // friends
    result = bars_each
    return result

print(solution())