def solution():
    hattie_round1 = 180
    lorelei_round1 = hattie_round1 * 3/4
    lorelei_round2 = hattie_round1 + 50
    hattie_round2 = hattie_round1 * 2/3

    total_round1 = hattie_round1 + lorelei_round1
    total_round2 = hattie_round2 + lorelei_round2
    total_jumps = total_round1 + total_round2

    return total_jumps

print(solution())