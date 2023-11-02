def solution():
    """Kimberley collects ten pounds of firewood, and Houston collects 12 pounds of firewood. If the three of them managed to collect a total of 35 pounds of firewood, how many pounds were collected by Ela?"""
    total_collected = 35
    kimberley_collected = 10
    houston_collected = 12
    ela_collected = total_collected - (kimberley_collected + houston_collected)
    result = ela_collected
    return result

print(solution())