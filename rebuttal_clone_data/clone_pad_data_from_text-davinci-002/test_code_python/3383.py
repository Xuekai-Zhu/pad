def solution():
    ads_blocked = 80
    ads_unblocked = 20
    ads_not_blocked_but_interested = ads_unblocked * 0.2
    ads_not_blocked_or_interested = ads_not_blocked_but_interested + ads_unblocked
    result = ads_not_blocked_or_interested
    return result

print(solution())