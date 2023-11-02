def solution():
    """A school is getting ready to open for the year and the sports class is organizing the equipment they have been donated. In total, they have 300 donations to organize. 60 of these were basketball hoops, half of which also had basketballs included as part of the donation. 120 pool floats were donated, but a quarter of these were damaged and were discarded before the sports class arrived. There were 50 footballs, 40 tennis balls, and the remaining donations were basketballs. In total, how many basketballs have been donated?"""
    basketball_hoops = 60
    basketball_hoops_with_basketballs = basketball_hoops / 2
    pool_floats = 120
    damaged_pool_floats = pool_floats / 4
    usable_pool_floats = pool_floats - damaged_pool_floats
    footballs = 50
    tennis_balls = 40
    total_basketballs = basketball_hoops_with_basketballs + usable_pool_floats + basketball_hoops_with_basketballs
    result = total_basketballs
    return result

print(solution())