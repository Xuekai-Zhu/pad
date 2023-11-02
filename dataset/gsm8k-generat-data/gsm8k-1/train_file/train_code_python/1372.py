def solution():
    """Jose bought 20,000 square meters of land and needs to divide it equally with his four siblings. How much land, in the square meters, will Jose have after dividing it with his siblings?"""
    total_land = 20000
    siblings = 4
    jose_land = total_land / (siblings + 1)
    result = jose_land
    return result

print(solution())