def solution():
    
    parker_share = 2
    richie_share = 3
    parker_amount = 50
    total_share = parker_share + richie_share
    richie_amount = parker_amount * (richie_share / parker_share)
    total_amount = parker_amount + richie_amount
    result = total_amount
    
    return result

print(solution())