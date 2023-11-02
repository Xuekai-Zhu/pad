def solution():
    # Calculate how many pins Richard knocked down in the first round
    richard_first_round = 70 + 15  # Richard knocked down 15 more pins than Patrick

    # Calculate how many pins Patrick knocked down in the second round
    patrick_second_round = 2 * richard_first_round

    # Calculate how many pins Richard knocked down in the second round
    richard_second_round = patrick_second_round - 3  # Richard knocked down 3 less than Patrick

    # Calculate the total number of pins knocked down by each person
    patrick_total = 70 + patrick_second_round
    richard_total = richard_first_round + richard_second_round

    # Calculate the difference in total pins knocked down by Patrick and Richard
    difference = richard_total - patrick_total
    result = difference
    return result

print(solution())