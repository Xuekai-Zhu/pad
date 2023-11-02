def solution():
    basketball_hoops = 60
    basketballs_in_hoops = basketball_hoops / 2
    damaged_pool_floats = 120 / 4
    undamaged_basketballs = 50 + 40  # 50 footballs and 40 tennis balls
    remaining_donations = 300 - (basketball_hoops + damaged_pool_floats + undamaged_basketballs)
    total_basketballs = basketballs_in_hoops + remaining_donations
    result = total_basketballs
    return result

print(solution())