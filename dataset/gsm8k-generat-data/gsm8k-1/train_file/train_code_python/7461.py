def solution():
    """Steve finds 100 gold bars while visiting Oregon. He wants to distribute his gold bars evenly to his 4 friends. If 20 gold bars were lost on the way back to San Diego, how many gold bars will each of his 4 friends get when he returns?"""
    initial_gold_bars = 100
    friends = 4
    lost_gold_bars = 20
    remaining_gold_bars = initial_gold_bars - lost_gold_bars
    gold_bars_per_friend = remaining_gold_bars // friends
    result = gold_bars_per_friend
    return result

print(solution())