def solution():
    
    parker_share = 2
    richie_share = 3
    total_share = parker_share + richie_share
    parker_amount = 50
    total_amount = parker_amount * total_share / parker_share
    result = total_amount
    return result

print(solution())