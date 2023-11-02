def solution():
    time_per_block = 1.5 / 2  # Justin can run 2 blocks in 1.5 minutes, so it takes him 0.75 minutes to run 1 block
    distance_to_home = 8  # Justin is 8 blocks from home

    # Calculate the total time it will take Justin to run home
    total_time = distance_to_home * time_per_block

    result = total_time
    return result

print(solution())