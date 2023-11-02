def solution():
    # Calculate the total time Frank has spent in corn mazes so far
    total_time = 4 * 50 + 45  # 4 other corn mazes finished in 50 minutes on average, and 45 minutes in the current maze

    # Calculate the maximum time Frank can spend in the current maze to maintain an average of 60 minutes per maze
    max_time = 60 * 5 - total_time  # Frank has to finish 5 mazes in total, and the average time per maze should be 60 minutes

    result = max_time
    return result

print(solution())