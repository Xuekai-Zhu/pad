def solution():
    num_lemons = 12
    fraction_given_away = 1/4

    # Calculate the number of lemons given away
    num_given_away = num_lemons * fraction_given_away

    # Calculate the number of lemons remaining with Cristine
    num_remaining = num_lemons - num_given_away
    result = num_remaining
    return result

print(solution())