def solution():
    total_donations = 300
    basketball_hoops = 60
    basketballs = basketball_hoops / 2
    pool_floats = 120
    damaged_floats = pool_floats / 4
    usable_floats = pool_floats - damaged_floats
    footballs = 50
    tennis_balls = 40
    remaining_donations = total_donations - (basketball_hoops + pool_floats + footballs + tennis_balls)
    result = basketballs + remaining_donations
    return result

print(solution())