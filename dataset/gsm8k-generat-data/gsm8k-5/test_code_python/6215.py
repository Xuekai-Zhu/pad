def solution():
    # Calculate the number of jumps Hattie did in the second round
    hattie_second_round = 2/3 * 180

    # Calculate the total number of jumps Hattie did
    hattie_total_jumps = 180 + hattie_second_round

    # Calculate the number of jumps Lorelei did in the first round
    lorelei_first_round = 3/4 * 180

    # Calculate the number of jumps Lorelei did in the second round
    lorelei_second_round = hattie_second_round + 50

    # Calculate the total number of jumps Lorelei did
    lorelei_total_jumps = lorelei_first_round + lorelei_second_round

    # Calculate the total number of jumps for both Hattie and Lorelei
    total_jumps = hattie_total_jumps + lorelei_total_jumps
    result = total_jumps
    return result

print(solution())