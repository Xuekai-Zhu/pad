def solution():
    march_bdays = 3
    oct_bdays = 1
    nov_bdays = 1
    dec_bdays = 2
    total_bdays = march_bdays + oct_bdays + nov_bdays + dec_bdays

    # Calculate the total number of presents for the first half of the year
    first_half_presents = total_bdays * 2

    # Calculate the total number of presents for the second half of the year
    second_half_presents = (7 * 2) - total_bdays

    # Calculate the difference between the two
    difference = second_half_presents - first_half_presents
    result = difference
    return result

print(solution())