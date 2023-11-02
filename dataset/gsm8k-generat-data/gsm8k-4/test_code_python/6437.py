def solution():
    """A factory uses robots to manufacture batteries. For each battery that is made, it takes a robot 6 minutes to gather the materials for the battery and 9 minutes to create the battery. If the factory has 10 robots working on batteries at the same time, how many batteries can the robots manufacture in 5 hours?"""
    # Define the time it takes for one robot to make one battery
    ONE_ROBOT_TIME = 6 + 9

    # Calculate the number of batteries one robot can make in one hour
    ONE_ROBOT_PER_HOUR = 60 / ONE_ROBOT_TIME

    # Calculate the number of batteries 10 robots can make in one hour
    TEN_ROBOTS_PER_HOUR = ONE_ROBOT_PER_HOUR * 10

    # Calculate the total number of batteries 10 robots can make in 5 hours
    TOTAL_BATTERIES = TEN_ROBOTS_PER_HOUR * 5

    # Return the result
    result = TOTAL_BATTERIES
    return result

print(solution())