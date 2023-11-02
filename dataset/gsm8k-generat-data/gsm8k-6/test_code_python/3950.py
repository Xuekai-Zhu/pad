def solution():
    # Calculate the number of matches won by the rival team
    rival_wins = 2 * 3  # the rival team has won twice as many matches as the home team

    # Calculate the total number of matches played
    total_matches = (3 + rival_wins + 4) * 2  # both teams have played the same number of matches (4 draws and no losses)

    result = total_matches
    return result

print(solution())