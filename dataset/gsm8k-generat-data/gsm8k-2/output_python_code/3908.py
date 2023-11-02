def solution():
    """John is performing in 3 plays. Each play has 5 Acts. He wears 2 wigs per act. Each wig cost $5. He drops one of the plays and sells all of the wigs for that play for $4. How much money did he spend?"""
    num_plays = 3
    num_acts_per_play = 5
    num_wigs_per_act = 2
    cost_per_wig = 5
    total_num_acts = num_plays * num_acts_per_play
    total_num_wigs = total_num_acts * num_wigs_per_act
    total_cost = total_num_wigs * cost_per_wig
    # Dropping one play
    total_num_wigs_dropped_play = num_acts_per_play * num_wigs_per_act
    total_cost_dropped_play = total_num_wigs_dropped_play * cost_per_wig * 0.8
    net_cost = total_cost - total_cost_dropped_play
    result = net_cost
    return result

print(solution())