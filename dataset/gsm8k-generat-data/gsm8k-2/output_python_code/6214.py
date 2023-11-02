def solution():
    """Hattie and her friend Lorelei are doing a jumping contest using a jumping rope. Hattie does 180 jumps in the first round, while Lorelei jumps 3/4 as many times as Hattie jumped. In the second round, Lorelei does 50 more jumps than Hattie. If Hattie managed to jump 2/3 times the number of jumps she did in the first round, calculate the total number of jumps the two did in the two rounds."""
    hattie_round1 = 180
    lorelei_round1 = 3/4 * hattie_round1
    lorelei_round2 = hattie_round2 + 50
    hattie_round2 = 2/3 * hattie_round1
    total_jumps = hattie_round1 + lorelei_round1 + hattie_round2 + lorelei_round2
    result = total_jumps
    return result

print(solution())