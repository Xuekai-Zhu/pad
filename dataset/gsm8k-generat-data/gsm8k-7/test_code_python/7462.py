def solution():
    num_gold_bars = 100
    num_friends = 4
    lost_bars = 20

    # Calculate the total number of gold bars after the loss
    total_gold_bars = num_gold_bars - lost_bars

    # Calculate the number of gold bars that each friend will receive
    num_bars_per_friend = total_gold_bars / num_friends
    result = num_bars_per_friend
    return result

print(solution())