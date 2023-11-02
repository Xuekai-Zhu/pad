def solution():
    num_cds = 21
    fraction_given_away = 1/3
    num_new_cds = 8

    # Calculate the number of CDs Tyler gives away
    num_given_away = num_cds * fraction_given_away

    # Calculate the number of CDs Tyler has left after giving some away
    num_left = num_cds - num_given_away

    # Calculate the total number of CDs Tyler has after buying some new ones
    num_total = num_left + num_new_cds
    result = num_total
    return result

print(solution())