def solution():
    """Larry started off having 150 channels from his cable company. They took 20 channels away and replaced those with 12 channels. He called the company and asked if he could reduce his package by 10 more channels but add the sports package which is 8 channels. He realizes that he didn't add the supreme sports package. He calls back and that package adds 7 more channels. How many channels does Larry have?"""
    initial_channels = 150
    channels_lost = 20
    channels_gained = 12
    channels_after_cable_change = initial_channels - channels_lost + channels_gained
    channels_removed = 10
    sports_package = 8
    supreme_sports_package = 7
    channels_after_package_change = channels_after_cable_change - channels_removed + sports_package + supreme_sports_package
    result = channels_after_package_change
    return result

print(solution())