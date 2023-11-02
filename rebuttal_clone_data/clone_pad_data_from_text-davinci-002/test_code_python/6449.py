def solution():
    goals_scored_by_carter = 4
    goals_scored_by_shelby = goals_scored_by_carter / 2
    goals_scored_by_judah = goals_scored_by_shelby * 2 - 3
    total_goals_scored = goals_scored_by_carter + goals_scored_by_shelby + goals_scored_by_judah
    average_goals_scored = total_goals_scored / 3
    result = average_goals_scored
    return result

print(solution())