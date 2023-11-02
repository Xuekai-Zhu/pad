def solution():
    # Calculate the number of fish caught in the second round
    second_round = 8 + 12  # Archer caught 12 more fish in the second round than the first round

    # Calculate the number of fish caught on the last round
    last_round = round(1.6 * second_round)  # Archer caught 60% more fish than in the second round

    # Calculate the total number of fish caught that day
    total_fish = 8 + second_round + last_round

    result = total_fish
    return result

print(solution())