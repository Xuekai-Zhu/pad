def solution():
    # Calculate the total volume of water that can splash out and evaporate before Jim has to clean the pool
    max_volume = 0.8 * 2000  # the pool needs to be refilled when it gets below 80% full
    remaining_volume = max_volume  # initial remaining volume is the maximum volume

    # Calculate the number of times people can jump in the pool before Jim has to clean it
    num_jumps = 0
    while remaining_volume >= 1.4:  # each jump causes 400 ml or 0.4 L of water to splash out and evaporate
        remaining_volume -= 0.4
        num_jumps += 1

    result = num_jumps
    return result

print(solution())