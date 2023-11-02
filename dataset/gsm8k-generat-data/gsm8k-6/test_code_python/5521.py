def solution():
    # Calculate the total time needed for the bread-making process
    total_time = 1 + (15/60) + 2 + (30/60) + (15/60)  # converting minutes to hours

    # Subtract the total time needed from the opening time (6:00 am) to get the latest start time
    latest_start_time = "5:" + "{0:0=2d}".format(int((60 * (6 - total_time)) % 60)) + " am"
    result = latest_start_time
    return result

print(solution())