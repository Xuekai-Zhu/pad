def solution():
    # Starting number of channels
    channels = 150

    # Subtract 20 channels and add 12
    channels = channels - 20 + 12

    # Subtract 10 channels and add the sports package
    channels = channels - 10 + 8

    # Add the supreme sports package
    channels = channels + 7

    result = channels
    return result

print(solution())