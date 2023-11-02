def solution():
    total_fights = 190
    knockouts_percentage = 0.5
    first_round_percentage = 0.2

    # Calculate the total number of knockouts
    total_knockouts = total_fights * knockouts_percentage

    # Calculate the number of knockouts in the first round
    first_round_knockouts = total_knockouts * first_round_percentage
    result = first_round_knockouts
    return result

print(solution())