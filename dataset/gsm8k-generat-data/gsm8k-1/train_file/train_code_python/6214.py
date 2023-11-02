def solution():
    """Hattie and her friend Lorelei are doing a jumping contest using a jumping rope. Hattie does 180 jumps in the first round, while Lorelei jumps 3/4 as many times as Hattie jumped. In the second round, Lorelei does 50 more jumps than Hattie. If Hattie managed to jump 2/3 times the number of jumps she did in the first round, calculate the total number of jumps the two did in the two rounds."""
    hattie_first_round = 180
    lorelei_first_round = hattie_first_round * 3/4
    lorelei_second_round = hattie_first_round + 50
    hattie_second_round = hattie_first_round * 2/3
    
    total_jumps = hattie_first_round + lorelei_first_round + hattie_second_round + lorelei_second_round
    result = total_jumps
    return result

print(solution())