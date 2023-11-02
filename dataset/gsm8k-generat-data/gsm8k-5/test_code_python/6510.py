def solution():
    # Calculate the total time it takes to create 4 speed painting videos
    total_time = 1 + (4*1) + 1 + (4*1.5)  # 1 hour set up, 4 hours painting, 1 hour clean up, 6 hours editing and posting

    # Calculate the time it takes to create one speed painting video
    time_per_video = total_time / 4
    result = time_per_video
    return result

print(solution())