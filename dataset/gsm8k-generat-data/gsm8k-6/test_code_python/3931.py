def solution():
    # Calculate the total number of goals scored by Gina and Tom
    goals_tom_day1 = 2 + 3  # Tom scored 3 more goals than Gina on the first day
    goals_tom_day2 = 6  # Tom scored 6 goals on the second day
    goals_gina_day1 = 2  # Gina scored 2 goals on the first day
    goals_gina_day2 = goals_tom_day2 - 2  # Gina scored 2 less than Tom on the second day
    total_goals = goals_tom_day1 + goals_tom_day2 + goals_gina_day1 + goals_gina_day2
    result = total_goals
    return result

print(solution())