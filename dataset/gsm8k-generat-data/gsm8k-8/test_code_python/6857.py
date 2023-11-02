def solution():
    # Calculate the total number of fish caught in the second round
    second_round = 8 + 12

    # Calculate the number of fish caught in the third round
    third_round = 1.6 * second_round

    # Calculate the total number of fish caught that day
    total_fish = 8 + second_round + third_round
    result = total_fish
    return result

print(solution())