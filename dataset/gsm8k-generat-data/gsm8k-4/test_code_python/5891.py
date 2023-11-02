def solution():
    """During the soccer match, The Kickers scored 2 goals in the first period and twice that amount in the second period. The other team, The Spiders, scored half the amount that The Kickers scored in the first period and twice the amount that The Kickers scored in their second period. What is the total amount of goals both teams scored?"""
    # Calculate the number of goals scored by The Kickers in the first period
    kickers_first_period = 2

    # Calculate the number of goals scored by The Kickers in the second period
    kickers_second_period = kickers_first_period * 2

    # Calculate the number of goals scored by The Spiders in the first period
    spiders_first_period = kickers_first_period / 2

    # Calculate the number of goals scored by The Spiders in the second period
    spiders_second_period = kickers_second_period * 2

    # Calculate the total number of goals scored by both teams
    total_goals = kickers_first_period + kickers_second_period + spiders_first_period + spiders_second_period

    # Return the result
    result = total_goals
    return result

print(solution())