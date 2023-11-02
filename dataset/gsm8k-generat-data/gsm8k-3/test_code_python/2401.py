def solution():
    """A wild tiger escapes the zoo.  He escapes at 1 AM and zookeepers do not notice he is missing until 4 AM.  He runs at a speed of 25 mph.  It takes 2 more hours to find him but after 4 hours of running, the tiger slows his speed to 10 mph.  He then gets chased for half an hour going 50 mph.  How far away from the zoo was he caught?"""
    # Calculate the distance the tiger ran before he was noticed missing
    distance_before_notice = 25 * 3 # Distance = Speed * Time

    # Calculate the distance the tiger ran before slowing down
    distance_before_slowing_down = 25 * 4 # Distance = Speed * Time

    # Calculate the distance the tiger ran while slowing down
    distance_while_slowing_down = 10 * 2 # Distance = Speed * Time

    # Calculate the distance the tiger was chased
    distance_chased = 50 * 0.5 # Distance = Speed * Time

    # Calculate the total distance the tiger ran
    total_distance = distance_before_notice + distance_before_slowing_down + distance_while_slowing_down + distance_chased

    # Display the total distance the tiger ran
    result = total_distance
    return result

print(solution())