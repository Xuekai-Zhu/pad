def solution():
    # Define the number of games Betsy won
    betsy_wins = 5

    # Calculate the number of games Helen won
    helen_wins = betsy_wins * 2

    # Calculate the number of games Susan won
    susan_wins = betsy_wins * 3

    # Calculate the total number of games won
    total_wins = betsy_wins + helen_wins + susan_wins

    result = total_wins
    return result

print(solution())