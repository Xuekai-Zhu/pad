def solution():
    """Mary, Jess, and Christina want to decorate a party room with balloons. Each person inflates balloons at different speeds, and they only have 30 minutes to inflate as many balloons as possible. Mary inflates 10 balloons per minute, Jess inflates 7 balloons per minute and Christina came 15 minutes late and was the slowest one inflating 4 balloons per minute. How many balloons can they inflate before running out of time?"""
    mary_speed = 10
    jess_speed = 7
    christina_speed = 4
    total_time = 30 # minutes
    christina_time = 15 # minutes
    mary_balloons = mary_speed * total_time
    jess_balloons = jess_speed * total_time
    christina_balloons = christina_speed * (total_time - christina_time)
    total_balloons = mary_balloons + jess_balloons + christina_balloons
    result = total_balloons
    return result

print(solution())