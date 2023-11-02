def solution():
    total_clovers = 500
    four_leaf_clovers_perc = 0.2
    purple_clovers_perc = 0.25

    # Calculate the number of four-leaved clovers
    num_four_leaf_clovers = total_clovers * four_leaf_clovers_perc

    # Calculate the number of four-leaved and purple clovers
    num_purple_and_four_leaf_clovers = num_four_leaf_clovers * purple_clovers_perc
    result = num_purple_and_four_leaf_clovers
    return result

print(solution())