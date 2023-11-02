def solution():
    initial_team_size = 25  # The initial team size is 25 people
    quitting_members = 8  # 8 people quit the team
    new_members = 13  # 13 new people joined the team

    # Calculate the new team size
    new_team_size = initial_team_size - quitting_members + new_members
    result = new_team_size
    return result

print(solution())