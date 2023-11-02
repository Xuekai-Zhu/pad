def solution():
    starting_channels = 150
    channels_removed = 20
    channels_added = 12
    channels_reduced = 10
    sports_package = 8
    supreme_sports_package = 7
    
    # Calculate the number of channels after the first change
    channels_after_first_change = starting_channels - channels_removed + channels_added
    
    # Calculate the number of channels after the second change
    channels_after_second_change = channels_after_first_change - channels_reduced + sports_package
    
    # Calculate the final number of channels after adding the supreme sports package
    final_channels = channels_after_second_change + supreme_sports_package
    
    result = final_channels
    return result

print(solution())