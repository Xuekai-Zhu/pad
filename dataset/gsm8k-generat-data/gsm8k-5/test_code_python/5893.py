def solution():
    total_time = 30  # They have 30 minutes to inflate balloons
    time_Christina = 15  # Christina came 15 minutes late
    time_left = total_time - time_Christina  # Time left for inflating balloons
    Mary_speed = 10  # Mary inflates 10 balloons per minute
    Jess_speed = 7  # Jess inflates 7 balloons per minute
    Christina_speed = 4  # Christina inflates 4 balloons per minute
    Christina_balloons = Christina_speed * (time_left)  # Christina will inflate balloons for (total_time - time_Christina) minutes
    Mary_balloons = Mary_speed * time_left  # Mary will inflate balloons for the entire time
    Jess_balloons = Jess_speed * time_left  # Jess will inflate balloons for the entire time

    # Calculate the total number of balloons inflated
    total_balloons = Christina_balloons + Mary_balloons + Jess_balloons
    result = total_balloons
    return result

print(solution())