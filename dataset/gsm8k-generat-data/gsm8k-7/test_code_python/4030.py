def solution():
    starting_difference = 10
    bailey_bands = 8
    
    # Calculate Justine's starting number of rubber bands
    justine_bands = bailey_bands + 2
    
    # Calculate Ylona's starting number of rubber bands
    ylona_bands = justine_bands + starting_difference + 2
    
    result = ylona_bands
    return result

print(solution())