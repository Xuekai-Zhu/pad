def solution():
    # Count the number of basketballs
    basketball_hoops = 60
    basketballs_with_hoops = basketball_hoops / 2
    pool_floats = 120
    damaged_pool_floats = pool_floats / 4
    usable_pool_floats = pool_floats - damaged_pool_floats
    footballs = 50
    tennis_balls = 40
    total_donations = 300

    basketballs = total_donations - basketball_hoops - usable_pool_floats - footballs - tennis_balls

    # Add the basketballs that were donated with the basketball hoops
    basketballs += basketballs_with_hoops

    result = basketballs
    return result

print(solution())