def solution():
    kickers_first_period_goals = 2
    kickers_second_period_goals = kickers_first_period_goals * 2
    spiders_first_period_goals = kickers_first_period_goals / 2
    spiders_second_period_goals = kickers_second_period_goals * 2

    # Calculate the total number of goals scored by both teams
    total_goals = kickers_first_period_goals + kickers_second_period_goals + spiders_first_period_goals + spiders_second_period_goals
    result = total_goals
    return result

print(solution())