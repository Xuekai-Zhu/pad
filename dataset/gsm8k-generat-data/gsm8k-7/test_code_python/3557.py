def solution():
    water_lost_per_jump = 0.4  # in liters
    pool_capacity = 2000  # in liters
    min_water_level = 0.8

    # Calculate the maximum amount of water that can be lost before the pool needs to be refilled
    max_water_loss = (1 - min_water_level) * pool_capacity

    # Calculate the number of times people can jump in the pool before Jim has to refill it
    num_jumps = max_water_loss / (water_lost_per_jump * 1000)

    result = int(num_jumps)  # convert to integer
    return result

print(solution())