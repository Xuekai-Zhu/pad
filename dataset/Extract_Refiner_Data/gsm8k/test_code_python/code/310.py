def solution():
    
    # Define the total number of players
    total_players = 105

    # Calculate the number of players on the defense
    defense_players = total_players / (1 + 0.5)

    # Display the number of players on the defense
    result = defense_players
    return result

print(solution())