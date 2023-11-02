def solution():
    # Define the number of group members and candy bars sold per member
    group_size = 20
    candy_bars_per_member = 8

    # Calculate total candy bars sold
    total_candy_bars = group_size * candy_bars_per_member

    # Calculate total earnings from candy bars sales
    total_earnings = total_candy_bars * 0.50
    result = total_earnings
    return result

print(solution())