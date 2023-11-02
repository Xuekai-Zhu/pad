def solution():
    """A factory uses robots to manufacture batteries. For each battery that is made, it takes a robot 6 minutes to gather the materials for the battery and 9 minutes to create the battery. If the factory has 10 robots working on batteries at the same time, how many batteries can the robots manufacture in 5 hours?"""
    # Calculate the total time it takes to make one battery
    total_time = 6 + 9

    # Calculate the number of batteries each robot can make in 5 hours
    batteries_per_robot = (5*60) // total_time

    # Calculate the total number of batteries that can be made by all 10 robots in 5 hours
    total_batteries = batteries_per_robot * 10

    # Display the total number of batteries that can be made in 5 hours
    result = total_batteries
    return result

print(solution())