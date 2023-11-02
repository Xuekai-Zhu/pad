def solution():
    """Gina and Tom were playing football. On the first day, Gina scored two goals, which was three less than Tom. On the second day, Gina scored two goals less than Tom who scored six goals. How many goals did Gina and Tom score during these two days?"""
    tom_first_day_goals = 2 + 3
    tom_second_day_goals = 6
    gina_first_day_goals = tom_first_day_goals - 3
    gina_second_day_goals = tom_second_day_goals - 2
    total_goals = tom_first_day_goals + tom_second_day_goals + gina_first_day_goals + gina_second_day_goals
    result = total_goals
    return result

print(solution())