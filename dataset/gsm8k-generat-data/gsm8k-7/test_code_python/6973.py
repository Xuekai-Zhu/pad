def solution():
    tank_capacity = 4000
    filling_rate = 10
    target_volume = tank_capacity * 3/4

    # Calculate the time it takes to fill the tank to the target volume
    time = target_volume / filling_rate
    result = time
    return result

print(solution())