def solution():
    """Kimberley collects ten pounds of firewood, and Houston collects 12 pounds of firewood. If the three of them managed to collect a total of 35 pounds of firewood, how many pounds were collected by Ela?"""
    kimberley_collect = 10
    houston_collect = 12
    total_collect = 35
    ela_collect = total_collect - kimberley_collect - houston_collect
    result = ela_collect
    return result

print(solution())