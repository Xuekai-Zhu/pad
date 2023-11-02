def solution():
    total_time = 2.5 + (3*0.5) + (20/60)  # Total time spent on all activities in hours
    time_watching_comet = 20/60  # Time spent watching the comet in hours

    # Calculate the percentage of total time spent watching the comet
    percentage_watching_comet = (time_watching_comet/total_time) * 100
    result = round(percentage_watching_comet)

    return result

print(solution())