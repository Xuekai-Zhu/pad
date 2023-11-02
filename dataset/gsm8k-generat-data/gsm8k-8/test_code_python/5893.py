def solution():
    total_time = 30
    mary_speed = 10
    jess_speed = 7
    christina_speed = 4
    christina_time = total_time - 15

    # Calculate how many balloons Mary and Jess can inflate in 30 minutes
    mj_balloons = (mary_speed + jess_speed) * total_time

    # Calculate how many balloons Christina can inflate in 15 minutes
    christina_balloons = christina_speed * christina_time

    # Calculate the total number of balloons they can inflate
    total_balloons = mj_balloons + christina_balloons
    result = total_balloons
    return result

print(solution())