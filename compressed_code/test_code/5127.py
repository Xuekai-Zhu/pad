def solution():
    
    initial_channels = 150
    removed_channels = 20
    added_channels = 12
    reduced_channels = 10
    sports_package = 8
    supreme_sports_package = 7
    
    
    new_channels = initial_channels - removed_channels + added_channels
    
    
    new_channels -= reduced_channels
    new_channels += sports_package
    
    
    new_channels += supreme_sports_package
    
    result = new_channels
    return result

print(solution())