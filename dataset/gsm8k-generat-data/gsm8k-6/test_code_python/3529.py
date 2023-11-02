def solution():
    # Calculate the number of supporters for the first and second teams
    support_first_team = 0.4 * 50 
    support_second_team = 0.34 * 50 

    # Calculate the number of people who didn't support either team
    not_supporting_either = 50 - support_first_team - support_second_team
    result = not_supporting_either
    return result

print(solution())