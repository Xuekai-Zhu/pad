def solution():
    # Calculate the number of goals scored by The Kickers in both periods
    goals_first_period = 2
    goals_second_period = 2 * 2  # twice the amount of goals in the first period

    # Calculate the number of goals scored by The Spiders in both periods
    spiders_first_period = goals_first_period / 2  # half the amount of goals scored by The Kickers in first period
    spiders_second_period = 2 * goals_second_period  # twice the amount of goals scored by The Kickers in second period

    # Calculate the total number of goals scored by both teams
    total_goals = goals_first_period + goals_second_period + spiders_first_period + spiders_second_period
    result = total_goals
    return result

print(solution())