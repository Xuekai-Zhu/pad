def solution():
    wigs_per_act = 2
    acts_per_play = 5
    number_of_plays = 3
    wig_cost = 5
    wigs_sold = wigs_per_act * acts_per_play
    wig_sale_price = 4
    total_cost = wig_cost * (number_of_plays * wigs_per_act - wigs_sold)
    result = total_cost
    return result

print(solution())