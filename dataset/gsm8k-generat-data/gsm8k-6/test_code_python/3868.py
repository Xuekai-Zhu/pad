def solution():
    starting_volume = 220  # liters
    lost_volume = 0.1 * starting_volume  # liters lost due to the leak
    remaining_volume = starting_volume - lost_volume  # liters remaining in the barrel
    result = remaining_volume
    return result

print(solution())