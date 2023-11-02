def solution():
    """During the soccer match, The Kickers scored 2 goals in the first period and twice that amount in the second period. The other team, The Spiders, scored half the amount that The Kickers scored in the first period and twice the amount that The Kickers scored in their second period. What is the total amount of goals both teams scored?"""
    kickers_first_period = 2
    kickers_second_period = kickers_first_period * 2
    spiders_first_period = kickers_first_period / 2
    spiders_second_period = kickers_second_period * 2
    kickers_total_goals = kickers_first_period + kickers_second_period
    spiders_total_goals = spiders_first_period + spiders_second_period
    total_goals = kickers_total_goals + spiders_total_goals
    result = total_goals
    return result

print(solution())