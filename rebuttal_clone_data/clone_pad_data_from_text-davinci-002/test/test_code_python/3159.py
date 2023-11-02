def solution():
    goals_first_half_A = 8
    goals_first_half_B = goals_first_half_A / 2
    goals_second_half_B = goals_first_half_A
    goals_second_half_A = goals_second_half_B - 2
    total_goals_A = goals_first_half_A + goals_second_half_A
    total_goals_B = goals_first_half_B + goals_second_half_B
    total_goals = total_goals_A + total_goals_B
    result = total_goals
    return result

print(solution())