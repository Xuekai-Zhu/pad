def solution():
    
    tom_first_day_goals = 2 + 3
    tom_second_day_goals = 6
    gina_first_day_goals = tom_first_day_goals - 3
    gina_second_day_goals = tom_second_day_goals - 2
    total_goals = tom_first_day_goals + tom_second_day_goals + gina_first_day_goals + gina_second_day_goals
    result = total_goals
    return result

print(solution())