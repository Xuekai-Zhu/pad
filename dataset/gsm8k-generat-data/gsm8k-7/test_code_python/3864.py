def solution():
    num_cookies = 20
    fraction_given_away = 2/5

    # Calculate the number of cookies given away
    num_given_away = num_cookies * fraction_given_away

    # Calculate the number of cookies left for Neil
    num_left = num_cookies - num_given_away
    result = num_left
    return result

print(solution())