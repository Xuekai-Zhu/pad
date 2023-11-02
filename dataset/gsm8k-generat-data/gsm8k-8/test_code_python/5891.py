def solution():
    # Calculate the number of goals The Kickers scored
    kickers_first_period = 2
    kickers_second_period = 2 * kickers_first_period
    kickers_total_goals = kickers_first_period + kickers_second_period

    # Calculate the number of goals The Spiders scored
    spiders_first_period = 0.5 * kickers_first_period
    spiders_second_period = 2 * kickers_second_period
    spiders_total_goals = spiders_first_period + spiders_second_period

    # Calculate the total number of goals scored by both teams
    total_goals = kickers_total_goals + spiders_total_goals
    result = total_goals
    return result

print(solution())