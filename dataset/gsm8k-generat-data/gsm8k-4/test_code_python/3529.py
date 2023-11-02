def solution():
    """During one game, a total of 50 people attended a baseball team’s games. Forty percent and thirty-four percent of the audiences are supporters of the first and second teams, respectively. How many people attended the game did not support either of the teams?"""
    # Define the total number of attendees
    total_attendees = 50

    # Calculate the number of attendees supporting the first team
    first_team_supporters = total_attendees * 0.4

    # Calculate the number of attendees supporting the second team
    second_team_supporters = total_attendees * 0.34

    # Calculate the number of attendees not supporting either team
    neither_supporters = total_attendees - first_team_supporters - second_team_supporters

    # return the result
    result = neither_supporters
    return result

print(solution())