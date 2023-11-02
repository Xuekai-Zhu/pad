def solution():
    
    total_cost = 2100
    sister_days = 4
    sue_days = 7 - sister_days
    sister_share = (sister_days / 7) * total_cost
    sue_share = total_cost - sister_share
    result = sue_share
    return result

print(solution())