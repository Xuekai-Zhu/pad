def solution():
    """Larry started off having 150 channels from his cable company. They took 20 channels away and replaced those with 12 channels. He called the company and asked if he could reduce his package by 10 more channels but add the sports package which is 8 channels. He realizes that he didn't add the supreme sports package. He calls back and that package adds 7 more channels. How many channels does Larry have?"""
    # Define the initial number of channels
    initial_channels = 150

    # Subtract the number of channels taken away and added
    new_channels = initial_channels - 20 + 12

    # Subtract 10 more channels and add the sports package
    new_channels -= 10
    new_channels += 8

    # Add the supreme sports package
    new_channels += 7

    # Return the result
    result = new_channels
    return result

print(solution())