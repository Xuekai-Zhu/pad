def solution():
    total_attendees = 50
    first_team_supporters = 0.4 * total_attendees
    second_team_supporters = 0.34 * total_attendees

    # Calculate the number of attendees who support both teams
    both_teams_supporters = 0.26 * total_attendees

    # Calculate the number of attendees who support neither team
    neither_team_supporters = total_attendees - (first_team_supporters + second_team_supporters - both_teams_supporters)
    result = neither_team_supporters
    return result

print(solution())