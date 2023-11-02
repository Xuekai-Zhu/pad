def solution():
     winning_team_first_quarter = 2 * 10
     winning_team_second_quarter = winning_team_first_quarter + 10
     winning_team_third_quarter = winning_team_second_quarter + 20
     winning_team_fourth_quarter = 80 - winning_team_third_quarter
     result = winning_team_fourth_quarter
     return result

print(solution())