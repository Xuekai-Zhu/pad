def solution():
    """Gina and Tom were playing football. On the first day, Gina scored two goals, which was three less than Tom. On the second day, Gina scored two goals less than Tom who scored six goals. How many goals did Gina and Tom score during these two days?"""
    gina_day1 = 2
    tom_day1 = gina_day1 + 3
    tom_day2 = 6
    gina_day2 = tom_day2 - 2
    total_goals = gina_day1 + tom_day1 + gina_day2 + tom_day2
    result = total_goals
    return result

print(solution())