def solution():
    # Calculate the distance Mr. Maxwell travels to work
    distance_to_work = 30  # Mr. Maxwell drives at an average speed of 30mph
    time_to_work = 1  # Mr. Maxwell takes 1 hour to drive to work
    distance_to_work = distance_to_work * time_to_work

    # Calculate the distance Mr. Maxwell travels back home
    distance_back_home = distance_to_work  # Mr. Maxwell drives the same distance back home

    # Calculate the average speed of Mr. Maxwell's return journey
    time_back_home = 1.5  # Mr. Maxwell takes 1.5 hours to drive back home
    average_speed = (distance_to_work + distance_back_home) / (time_to_work + time_back_home)
    result = average_speed
    return result

print(solution())