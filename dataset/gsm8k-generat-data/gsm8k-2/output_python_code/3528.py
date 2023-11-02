def solution():
    """During one game, a total of 50 people attended a baseball team’s games. Forty percent and thirty-four percent of the audiences are supporters of the first and second teams, respectively. How many people attended the game did not support either of the teams?"""
    total_people = 50
    first_team_supporters = 0.4 * total_people
    second_team_supporters = 0.34 * total_people
    neither_supporters = total_people - first_team_supporters - second_team_supporters
    result = neither_supporters
    return result

print(solution())