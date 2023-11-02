def solution():
    
    total_packs = 80
    expired_packs = total_packs * 0.4
    non_expired_packs = total_packs - expired_packs
    pack_price = 12
    refund_amount = expired_packs * pack_price
    result = refund_amount
    return result

print(solution())