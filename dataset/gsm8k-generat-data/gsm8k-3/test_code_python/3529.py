def solution():
    """During one game, a total of 50 people attended a baseball team’s games. Forty percent and thirty-four percent of the audiences are supporters of the first and second teams, respectively. How many people attended the game did not support either of the teams?"""
    # Define the total number of people who attended the game
    total_attendees = 50

    # Calculate the number of people who support the first team
    first_team_supporters = total_attendees * 0.4

    # Calculate the number of people who support the second team
    second_team_supporters = total_attendees * 0.34

    # Calculate the number of people who don't support either team
    neither_team_supporters = total_attendees - first_team_supporters - second_team_supporters

    # Display the number of people who don't support either team
    result = neither_team_supporters
    return result

print(solution())