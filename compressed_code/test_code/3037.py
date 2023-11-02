def solution():
    
    num_plays = 3
    num_acts_per_play = 5
    num_wigs_per_act = 2
    cost_per_wig = 5
    total_num_acts = num_plays * num_acts_per_play
    total_num_wigs = total_num_acts * num_wigs_per_act
    total_cost = total_num_wigs * cost_per_wig
    
    total_num_wigs_dropped_play = num_acts_per_play * num_wigs_per_act
    total_cost_dropped_play = total_num_wigs_dropped_play * cost_per_wig * 0.8
    net_cost = total_cost - total_cost_dropped_play
    result = net_cost
    return result

print(solution())