def solution():
    time_per_four_windows = 10  # David takes 10 minutes to wash 4 windows
    total_windows = 64  # David's house has 64 windows

    # Calculate the total time David will spend washing all the windows
    total_time = (total_windows / 4) * time_per_four_windows

    result = total_time
    return result

print(solution())