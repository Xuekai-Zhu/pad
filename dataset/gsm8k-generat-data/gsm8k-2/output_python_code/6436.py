def solution():
    """A factory uses robots to manufacture batteries. For each battery that is made, it takes a robot 6 minutes to gather the materials for the battery and 9 minutes to create the battery. If the factory has 10 robots working on batteries at the same time, how many batteries can the robots manufacture in 5 hours?"""
    gather_time = 6
    create_time = 9
    total_time = gather_time + create_time
    batteries_per_hour = 60 / total_time
    robots = 10
    total_batteries = batteries_per_hour * 5 * robots
    result = total_batteries
    return result

print(solution())