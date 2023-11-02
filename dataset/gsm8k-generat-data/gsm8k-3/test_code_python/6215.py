def solution():
    """Hattie and her friend Lorelei are doing a jumping contest using a jumping rope. Hattie does 180 jumps in the first round, while Lorelei jumps 3/4 as many times as Hattie jumped. In the second round, Lorelei does 50 more jumps than Hattie. If Hattie managed to jump 2/3 times the number of jumps she did in the first round, calculate the total number of jumps the two did in the two rounds."""
    # Hattie's jumps in the first round
    hattie_round1_jumps = 180

    # Lorelei's jumps in the first round
    lorelei_round1_jumps = hattie_round1_jumps * 3 / 4

    # Hattie's jumps in the second round
    hattie_round2_jumps = hattie_round1_jumps * 2 / 3

    # Lorelei's jumps in the second round
    lorelei_round2_jumps = hattie_round2_jumps + 50

    # Total number of jumps in the two rounds
    total_jumps = hattie_round1_jumps + lorelei_round1_jumps + hattie_round2_jumps + lorelei_round2_jumps

    # Display the total number of jumps
    result = total_jumps
    return result

print(solution())