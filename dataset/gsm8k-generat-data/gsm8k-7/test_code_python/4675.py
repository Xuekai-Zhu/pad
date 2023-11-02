def solution():
    num_knives = 6
    num_forks = 12
    num_spoons = 3 * num_knives

    # Adjust for the friend's trade
    num_knives += 10
    num_spoons -= 6

    # Calculate the total number of pieces of silverware
    total_pieces = num_knives + num_forks + num_spoons

    # Calculate the percentage of silverware that is knives
    percent_knives = (num_knives / total_pieces) * 100
    result = percent_knives
    return result

print(solution())