def solution():
    total_packs = 80
    percentage_expired = 40
    expired_packs = total_packs * (percentage_expired / 100)
    cost_per_pack = 12
    refund = expired_packs * cost_per_pack
    result = refund
    return result

print(solution())