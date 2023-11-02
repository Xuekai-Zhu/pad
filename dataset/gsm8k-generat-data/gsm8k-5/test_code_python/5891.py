def solution():
    kickers_first_period = 2  # The Kickers scored 2 goals in the first period
    kickers_second_period = 2 * kickers_first_period  # The Kickers scored twice as many goals in the second period
    spiders_first_period = 0.5 * kickers_first_period  # The Spiders scored half as many goals as The Kickers in the first period
    spiders_second_period = 2 * kickers_second_period  # The Spiders scored twice as many goals as The Kickers in the second period

    # Calculate the total amount of goals scored by both teams
    total_goals = kickers_first_period + kickers_second_period + spiders_first_period + spiders_second_period
    result = total_goals
    return result

print(solution())