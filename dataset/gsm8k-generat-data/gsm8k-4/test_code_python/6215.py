def solution():
    """Hattie and her friend Lorelei are doing a jumping contest using a jumping rope. Hattie does 180 jumps in the first round, while Lorelei jumps 3/4 as many times as Hattie jumped. In the second round, Lorelei does 50 more jumps than Hattie. If Hattie managed to jump 2/3 times the number of jumps she did in the first round, calculate the total number of jumps the two did in the two rounds."""
    # Calculate the number of jumps Hattie did in the first round
    hattie_round1 = 180

    # Calculate the number of jumps Lorelei did in the first round
    lorelei_round1 = hattie_round1 * 3/4

    # Calculate the number of jumps Hattie did in the second round
    hattie_round2 = hattie_round1 * 2/3

    # Calculate the number of jumps Lorelei did in the second round
    lorelei_round2 = hattie_round2 + 50

    # Calculate the total number of jumps
    total_jumps = hattie_round1 + lorelei_round1 + hattie_round2 + lorelei_round2

    # Return the result
    result = total_jumps
    return result

print(solution())