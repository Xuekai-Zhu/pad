def solution():
    
    basketball_hoops = 60
    basketballs_with_hoops = basketball_hoops / 2
    damaged_pool_floats = 120 / 4
    pool_floats = 120 - damaged_pool_floats
    basketballs = (300 - basketball_hoops - pool_floats - 50 - 40) + basketballs_with_hoops
    result = basketballs
    return result

print(solution())