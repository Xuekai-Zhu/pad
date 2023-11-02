def solution():
    """Jonsey is awake for 2/3 of the day and spends 1/2 her time awake playing outside and the rest inside. 
    Her brother, Riley, is awake for 3/4 of the day and spends 1/3 of his day outside and the rest inside. 
    How much time, on average, do they spend inside?"""
    jonesy_awake_time = (2/3) * 24  # total number of hours in a day = 24
    jonesy_outside_time = (1/2) * jonesy_awake_time
    jonesy_inside_time = jonesy_awake_time - jonesy_outside_time

    riley_awake_time = (3/4) * 24
    riley_outside_time = (1/3) * riley_awake_time
    riley_inside_time = riley_awake_time - riley_outside_time

    total_inside_time = jonesy_inside_time + riley_inside_time
    average_inside_time = total_inside_time / 2

    result = average_inside_time
    return result

print(solution())