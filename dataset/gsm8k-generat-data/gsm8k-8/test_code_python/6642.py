def solution():
    # Starting channels
    starting_channels = 150

    # Channels after first adjustment
    channels_after_first = starting_channels - 20 + 12

    # Channels after second adjustment
    channels_after_second = channels_after_first - 10 + 8 + 7

    # Total channels Larry has
    total_channels = channels_after_second
    result = total_channels
    return result

print(solution())