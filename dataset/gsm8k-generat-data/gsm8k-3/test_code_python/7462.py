def solution():
    """Steve finds 100 gold bars while visiting Oregon. He wants to distribute his gold bars evenly to his 4 friends. If 20 gold bars were lost on the way back to San Diego, how many gold bars will each of his 4 friends get when he returns?"""
    # Define the number of gold bars found and the number of friends
    GOLD_BARS_FOUND = 100
    NUM_FRIENDS = 4

    # Subtract the lost gold bars from the total
    remaining_gold_bars = GOLD_BARS_FOUND - 20

    # Calculate the number of gold bars each friend will get
    bars_per_friend = remaining_gold_bars // NUM_FRIENDS

    # Display the number of gold bars each friend will get
    result = bars_per_friend
    return result

print(solution())