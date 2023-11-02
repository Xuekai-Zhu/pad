def solution():
    balloons = 1000
    balloon_capacity = 10
    total_liters = balloons * balloon_capacity
    gas_tanks = total_liters / 500
    result = gas_tanks
    return result

print(solution())