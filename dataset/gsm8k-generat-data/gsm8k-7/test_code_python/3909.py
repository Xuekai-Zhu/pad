def solution():
    num_plays = 3
    acts_per_play = 5
    wigs_per_act = 2
    cost_per_wig = 5

    # Calculate the total number of acts for all plays
    total_acts = num_plays * acts_per_play

    # Calculate the total number of wigs needed for all plays
    total_wigs = total_acts * wigs_per_act

    # Calculate the total cost of all wigs
    total_wig_cost = total_wigs * cost_per_wig

    # Subtract the cost of the wigs sold for the dropped play
    total_wig_cost -= 4 * (acts_per_play * wigs_per_act)

    result = total_wig_cost
    return result

print(solution())