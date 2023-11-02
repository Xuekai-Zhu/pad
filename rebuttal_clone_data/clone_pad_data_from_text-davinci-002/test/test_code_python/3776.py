def solution():
    primary_tank = 2
    supplemental_tank = 1
    total_time = 8
    total_tanks = (total_time - primary_tank) / supplemental_tank
    result = total_tanks
    return result

print(solution())