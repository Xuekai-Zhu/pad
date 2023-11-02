def solution():
    # Calculate Lorelei's jumps in the first round
    lorelei_jumps_round1 = (3/4) * 180  

    # Calculate Hattie's jumps in the second round
    hattie_jumps_round2 = (2/3) * 180  

    # Calculate Lorelei's jumps in the second round
    lorelei_jumps_round2 = hattie_jumps_round2 + 50  

    # Calculate the total number of jumps
    total_jumps = 180 + lorelei_jumps_round1 + hattie_jumps_round2 + lorelei_jumps_round2
    result = total_jumps
    return result

print(solution())