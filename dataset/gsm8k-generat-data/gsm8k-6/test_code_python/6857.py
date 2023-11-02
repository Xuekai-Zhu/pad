def solution():
    # Calculate the total number of fish caught by Archer that day
    first_round = 8  # number of fish caught in the first round
    second_round = first_round + 12  # number of fish caught in the second round
    third_round = 1.6 * second_round  # number of fish caught in the third round, 60% more than second round
    total_fish = first_round + second_round + third_round  # total number of fish caught
    result = total_fish
    return result

print(solution())