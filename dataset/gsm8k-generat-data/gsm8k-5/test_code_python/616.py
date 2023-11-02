def solution():
    kris_speed = 2  # Kris can blow up 2 balloons per minute
    brother_speed = 2 * kris_speed  # Kris's brother works twice as fast as Kris
    total_time = 30  # Kris and her brother have 30 minutes to blow up balloons

    # Calculate how many balloons Kris and her brother can blow up in the first 15 minutes
    balloons_in_15_minutes = (kris_speed + brother_speed) * 15

    # Double the brother's speed for the remaining 15 minutes
    brother_speed *= 2

    # Calculate how many balloons Kris and her brother can blow up in the remaining 15 minutes
    balloons_in_remaining_time = (kris_speed + brother_speed) * 15

    # Calculate the total number of balloons Kris and her brother have blown up in 30 minutes
    total_balloons = balloons_in_15_minutes + balloons_in_remaining_time
    result = total_balloons
    return result

print(solution())