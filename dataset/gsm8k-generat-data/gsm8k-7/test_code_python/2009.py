def solution():
    total_members = 110
    
    # Let x be the number of brass players
    x = total_members / 7
    
    # Calculate the number of woodwind players
    num_woodwinds = x / 2
    
    # Calculate the number of percussion players
    num_percussions = num_woodwinds * 4
    
    # Calculate the total number of brass players
    total_brass_players = x
    
    result = total_brass_players
    return result

print(solution())