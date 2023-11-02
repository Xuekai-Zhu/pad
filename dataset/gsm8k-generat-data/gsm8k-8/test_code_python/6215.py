def solution():
    # Calculate the number of jumps Lorelei did in the first round
    lorelei_round1 = 0.75 * 180

    # Calculate the number of jumps Hattie did in the second round
    hattie_round2 = 2/3 * 180

    # Calculate the number of jumps Lorelei did in the second round
    lorelei_round2 = hattie_round2 + 50

    # Calculate the total number of jumps in both rounds
    total_jumps = 180 + lorelei_round1 + hattie_round2 + lorelei_round2
    result = total_jumps
    return result

print(solution())