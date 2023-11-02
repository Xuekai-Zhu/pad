def solution():
    # Define the number of percussion players as 4 times the number of woodwind players
    percussion_players = 4 * woodwind_players

    # Define the number of woodwind players as twice the number of brass players
    woodwind_players = 2 * brass_players

    # Set up an equation using the total number of band members and solve for the number of brass players
    total_members = percussion_players + woodwind_players + brass_players
    brass_players = (total_members - percussion_players - woodwind_players) / 3

    result = brass_players
    return result

print(solution())