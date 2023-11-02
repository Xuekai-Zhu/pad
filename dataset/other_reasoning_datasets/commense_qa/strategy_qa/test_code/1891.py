def solution():
    # Define the number of teams and wrestlers needed for a complete tag team match
    min_teams = 2
    min_wrestlers_per_team = 2
    # Define the number of Powerpuff Girls
    powerpuff_girls_num = 3
    # Check if the Powerpuff Girls can form a complete tag team match
    if powerpuff_girls_num >= min_teams*min_wrestlers_per_team:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())