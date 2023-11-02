def solution():
    plays = 3  # John is performing in 3 plays
    acts_per_play = 5  # Each play has 5 acts
    wigs_per_act = 2  # John wears 2 wigs per act
    wig_cost = 5  # Each wig costs $5
    dropped_play = 1  # John drops the first play and sells all of the wigs for that play for $4

    # Calculate the total number of wigs John wears in all plays
    total_wigs = plays * acts_per_play * wigs_per_act

    # Calculate the total cost of all the wigs John wears in all plays
    total_wig_cost = total_wigs * wig_cost

    # Calculate the amount John receives from selling the wigs for the dropped play
    dropped_wig_cost = acts_per_play * wigs_per_act * wig_cost
    total_money_received = dropped_wig_cost * 4

    # Calculate John's total expenditure
    total_expenditure = total_wig_cost - total_money_received
    result = total_expenditure
    return result

print(solution())