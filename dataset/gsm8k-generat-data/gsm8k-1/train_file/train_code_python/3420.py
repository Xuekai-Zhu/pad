def solution():
    """Sam has 3 German Shepherds and 4 French Bulldogs. Peter wants to buy 3 times as many German Shepherds as Sam has and 2 times as many French Bulldogs as Sam has. How many dogs does Peter want to have?"""
    sam_gs = 3
    sam_fb = 4
    peter_gs = sam_gs * 3
    peter_fb = sam_fb * 2
    total_dogs = peter_gs + peter_fb
    result = total_dogs
    return result

print(solution())