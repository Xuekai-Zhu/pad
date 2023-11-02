def solution():
    total_players = 24
    first_half_starters = 11
    first_half_substitutions = 2

    # Calculate the number of players who participated in the first half
    first_half_total = first_half_starters + first_half_substitutions

    # Calculate the number of players remaining for the second half
    second_half_remaining = total_players - first_half_total

    # Calculate the number of substitutions made in the second half
    second_half_substitutions = first_half_substitutions * 2

    # Calculate the number of players who participated in the second half including substitutions
    second_half_total = first_half_starters + second_half_substitutions

    # Calculate the number of players who did not play
    num_non_players = total_players - second_half_total
    result = num_non_players
    return result

print(solution())