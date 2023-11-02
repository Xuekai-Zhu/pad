def solution():
    time_rising = 120 * 2  # Mark has to let the bread rise for 120 minutes twice
    time_kneading = 10  # Mark needs to spend 10 minutes kneading the bread
    time_baking = 30  # Mark needs to spend 30 minutes baking the bread

    # Calculate the total time it takes Mark to finish making the bread
    total_time = time_rising + time_kneading + time_baking
    result = total_time
    return result

print(solution())