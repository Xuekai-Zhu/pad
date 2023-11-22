def solution():
    
    # Define the number of schools and the number of players per team
    NUM_SCHOOLS = 4
    PLAYERS_PER_TEAM = 5

    # Calculate the total number of players
    total_players = NUM_SCHOOLS * PLAYERS_PER_TEAM

    # Calculate the total number of coaches
    total_coaches = NUM_SCHOOLS * 2

    # Calculate the total number of people
    total_people = total_players + total_coaches

    # Display the total number of people
    result = total_people
    return result

print(solution())