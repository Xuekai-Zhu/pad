def solution():
    # Calculate the time it takes for each runner to run their portion of the race
    time_Rhonda = 24
    time_Sally = time_Rhonda + 2
    time_Diane = time_Rhonda - 3

    # Calculate the total time it takes for all three runners to complete the race
    total_time = time_Rhonda + time_Sally + time_Diane
    result = total_time
    return result

print(solution())