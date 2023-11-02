def solution():
    # Calculate Patrick's score in the first round
    patrick_first_round = 70
    # Calculate Richard's score in the first round
    richard_first_round = patrick_first_round + 15
    # Calculate Patrick's score in the second round
    patrick_second_round = richard_first_round * 2
    # Calculate Richard's score in the second round
    richard_second_round = patrick_second_round - 3
    # Calculate the total number of pins knocked down by Patrick
    patrick_total = patrick_first_round + patrick_second_round
    # Calculate the total number of pins knocked down by Richard
    richard_total = richard_first_round + richard_second_round
    # Calculate the difference between Richard's and Patrick's total scores
    difference = richard_total - patrick_total
    result = difference
    return result

print(solution())