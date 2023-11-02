def solution():
    """Three teenagers are playing soccer on the weekend. Richie, the first teenager, scored 20 more goals than Mark and scored 45 more goals than Anna. If Richie scored 80 goals, how many goals did all three teenagers score?"""
    richie_goals = 80
    mark_goals = richie_goals - 20
    anna_goals = mark_goals - 45
    total_goals = richie_goals + mark_goals + anna_goals
    result = total_goals
    return result

print(solution())