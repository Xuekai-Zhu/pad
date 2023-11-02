def solution():
    """Steve finds 100 gold bars while visiting Oregon. He wants to distribute his gold bars evenly to his 4 friends. If 20 gold bars were lost on the way back to San Diego, how many gold bars will each of his 4 friends get when he returns?"""
    # Define the initial number of gold bars
    initial_bars = 100

    # Define the number of friends to distribute gold to
    num_friends = 4

    # Define the number of lost gold bars
    lost_bars = 20

    # Calculate the total number of gold bars after accounting for loss
    total_bars = initial_bars - lost_bars

    # Calculate the number of gold bars that each friend will receive
    bars_per_friend = total_bars // num_friends

    # Return the result
    result = bars_per_friend
    return result

print(solution())