def solution():
    
    kickers_first_period = 2
    kickers_second_period = 2 * kickers_first_period
    spiders_first_period = 0.5 * kickers_first_period
    spiders_second_period = 2 * kickers_second_period
    total_goals = kickers_first_period + kickers_second_period + spiders_first_period + spiders_second_period
    result = total_goals
    return result

print(solution())