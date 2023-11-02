def solution():
    mary_speed = 10
    jess_speed = 7
    christina_speed = 4

    total_time = 30  # in minutes
    christina_arrival_time = 15  # in minutes

    # Calculate the total number of balloons Mary and Jess can inflate in 30 minutes
    mary_balloons = mary_speed * total_time
    jess_balloons = jess_speed * total_time

    # Calculate the total number of balloons Christina can inflate in 15 minutes
    christina_balloons = christina_speed * (total_time - christina_arrival_time)

    # Calculate the total number of balloons all three can inflate before running out of time
    total_balloons = mary_balloons + jess_balloons + christina_balloons
    result = total_balloons
    return result

print(solution())