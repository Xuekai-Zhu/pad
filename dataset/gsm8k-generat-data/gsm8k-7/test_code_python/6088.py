def solution():
    num_shirts = 4 * 12  # 4 dozen = 48 shirts
    fraction_given_away = 1/3
    num_given_away = num_shirts * fraction_given_away

    # Calculate the number of shirts left
    num_left = num_shirts - num_given_away
    result = num_left
    return result

print(solution())