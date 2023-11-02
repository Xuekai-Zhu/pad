def solution():
    jessa_bills = 7  # Jessa has 7 bills left after giving 3 bills to Geric
    kyla_bills = jessa_bills + 2  # Kyla has two fewer bills than Jessa
    geric_bills = 2 * kyla_bills  # Geric has twice as many bills as Kyla
    
    # Geric received 3 bills from Jessa, so his total number of bills is:
    geric_bills += 3
    
    result = geric_bills
    return result

print(solution())