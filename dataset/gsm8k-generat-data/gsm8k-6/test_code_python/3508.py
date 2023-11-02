def solution():
    # Calculate the distance Mr. Maxwell drives to work
    distance_to_work = 30  # he drives at an average speed of 30mph
    time_to_work = 1  # it takes him 1 hr to drive to work
    distance_to_work = distance_to_work * time_to_work

    # Calculate the average speed of Mr. Maxwell's return journey
    time_to_home = 1.5  # it takes him 1.5 hrs to drive back home
    distance_to_home = distance_to_work  # assuming the distance is the same
    speed_on_return = distance_to_home / time_to_home
    result = speed_on_return

    return result

print(solution())