def solution():
    # Define the number of wins for the rival team
    rival_wins = 2 * 3

    # Calculate the total number of matches played by both teams
    total_matches = 2 * (3 + 4 + 0) # 2 teams playing 7 matches each

    # Add the number of wins for both teams to the total matches
    total_matches += 3 + rival_wins

    result = total_matches
    return result

print(solution())