def solution():
    # Calculate the number of pins knocked down by Patrick in the second round
    patrick_second_round = 2 * (70 + 15)  # Patrick knocked down twice as many pins as Richard in the first round

    # Calculate the number of pins knocked down by Richard in the second round
    richard_second_round = patrick_second_round - 3  # Richard knocked down 3 less than Patrick

    # Calculate the total number of pins knocked down by each person
    patrick_total = 70 + patrick_second_round
    richard_total = 70 + 15 + richard_second_round

    # Calculate the difference in total number of pins knocked down between Richard and Patrick
    difference = richard_total - patrick_total
    result = difference
    return result

print(solution())