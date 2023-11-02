def solution():
    # Calculate the number of people who support the first team
    first_team_supporters = 0.4 * 50

    # Calculate the number of people who support the second team
    second_team_supporters = 0.34 * 50

    # Calculate the total number of people who support either team
    total_supporters = first_team_supporters + second_team_supporters

    # Calculate the number of people who do not support either team
    non_supporters = 50 - total_supporters
    result = non_supporters
    return result

print(solution())