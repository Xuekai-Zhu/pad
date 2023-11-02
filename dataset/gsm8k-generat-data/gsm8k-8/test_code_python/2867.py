def solution():
    # Define the speed ratios
    micah_to_dean = 2/3
    jake_to_micah = 4/3

    # Calculate Micah's time
    micah_time = (1/micah_to_dean) * 9

    # Calculate Jake's time
    jake_time = (1/jake_to_micah) * micah_time

    # Calculate the total time
    total_time = micah_time + jake_time + 9

    result = total_time
    return result

print(solution())