def solution():
    """Larry started off having 150 channels from his cable company. They took 20 channels away and replaced those with 12 channels. He called the company and asked if he could reduce his package by 10 more channels but add the sports package which is 8 channels. He realizes that he didn't add the supreme sports package. He calls back and that package adds 7 more channels. How many channels does Larry have?"""
    initial_channels = 150
    removed_channels = 20
    added_channels = 12
    reduced_channels = 10
    sports_package = 8
    supreme_sports_package = 7
    
    # Subtract removed channels and add added channels
    new_channels = initial_channels - removed_channels + added_channels
    
    # Subtract reduced channels and add sports package
    new_channels -= reduced_channels
    new_channels += sports_package
    
    # Add supreme sports package
    new_channels += supreme_sports_package
    
    result = new_channels
    return result

print(solution())