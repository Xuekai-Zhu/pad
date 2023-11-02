def solution():
    """A wild tiger escapes the zoo. He escapes at 1 AM and zookeepers do not notice he is missing until 4 AM. He runs at a speed of 25 mph. It takes 2 more hours to find him but after 4 hours of running, the tiger slows his speed to 10 mph. He then gets chased for half an hour going 50 mph. How far away from the zoo was he caught?"""
    # Define the time the tiger runs before getting noticed by zookeepers
    time_before_noticed = 3 # in hours

    # Define the initial speed and time of the tiger
    initial_speed = 25 # in mph
    initial_time = time_before_noticed # in hours

    # Calculate the distance the tiger runs before getting noticed
    distance_before_noticed = initial_speed * initial_time

    # Define the time it takes to find the tiger
    time_to_find = 2 # in hours

    # Define the speed of the tiger after being found
    found_speed = 10 # in mph

    # Define the time the tiger is chased
    chase_time = 0.5 # in hours

    # Define the speed of the chase
    chase_speed = 50 # in mph

    # Calculate the distance the tiger runs before being caught
    distance_before_caught = distance_before_noticed + found_speed * (time_to_find + 4 - initial_time) + chase_speed * chase_time

    result = distance_before_caught
    return result

print(solution())