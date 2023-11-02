def solution():
    """John is performing in 3 plays. Each play has 5 Acts. He wears 2 wigs per act. Each wig cost $5. He drops one of the plays and sells all of the wigs for that play for $4. How much money did he spend?"""
    plays = 3
    acts_per_play = 5
    wigs_per_act = 2
    wig_cost = 5
    wigs_for_dropped_play = acts_per_play * wigs_per_act
    total_wigs = (plays * acts_per_play * wigs_per_act) - wigs_for_dropped_play
    total_cost = total_wigs * wig_cost
    income_from_dropped_wigs = wigs_for_dropped_play * 4
    money_spent = total_cost - income_from_dropped_wigs
    result = money_spent
    return result

print(solution())