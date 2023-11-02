def solution():
    # Calculate the total time spent on all activities
    total_time = 2.5 + (3 * 0.5) + 0.3333 + 0.3333  # shopping time + setup time + snack time + comet watching time
    comet_time = 0.3333  # time spent watching the comet
    percent_comet_time = round((comet_time / total_time) * 100)  # calculate the percentage of time spent watching the comet and round to nearest percent
    result = percent_comet_time
    return result

print(solution())