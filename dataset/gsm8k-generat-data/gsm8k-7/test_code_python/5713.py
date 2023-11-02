def solution():
    tina_time = 6 # in minutes
    tom_time = tina_time / (1/3) # in minutes
    tony_time = tina_time / 2 # in minutes

    # Convert all times to seconds
    tina_time_sec = tina_time * 60
    tom_time_sec = tom_time * 60
    tony_time_sec = tony_time * 60

    # Calculate the total time for all three runners
    total_time_sec = tina_time_sec + tom_time_sec + tony_time_sec

    # Convert the total time back to minutes and seconds
    total_time_min = total_time_sec // 60
    total_time_sec_remain = total_time_sec % 60

    result = f"{total_time_min}:{total_time_sec_remain:02d}" # format the result as "min:sec"
    return result

print(solution())