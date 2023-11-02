def solution():
    total_attendees = 50  # Total number of people who attended the game
    first_team_supporters = 0.4 * total_attendees  # 40% of attendees support the first team
    second_team_supporters = 0.34 * total_attendees  # 34% of attendees support the second team

    # Calculate the number of attendees who did not support either team
    non_supporters = total_attendees - first_team_supporters - second_team_supporters
    result = non_supporters
    return result

print(solution())