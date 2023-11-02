def solution():
    time_to_gather = 6 # Time taken by a robot to gather materials for a battery
    time_to_manufacture = 9 # Time taken by a robot to manufacture a battery 
    total_time = (5 * 60) # Total time in minutes for 5 hours 
    robots_count = 10 # Total number of robots working on batteries simultaneously 

    # Total time taken by a robot to make a battery
    total_time_per_battery = time_to_gather + time_to_manufacture 

    # Total number of batteries the 10 robots can manufacture in 5 hours 
    total_batteries = (total_time // total_time_per_battery) * robots_count 

    result = total_batteries
    return result

print(solution())