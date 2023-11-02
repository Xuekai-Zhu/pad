def solution():
    # Calculate the time taken by one robot to make one battery
    time_per_battery = 6 + 9  # 6 minutes to gather materials and 9 minutes to create battery

    # Calculate the number of batteries that can be made by one robot in 5 hours
    batteries_per_robot = int(5 * 60 / time_per_battery)

    # Calculate the total number of batteries that can be made by all 10 robots in 5 hours
    total_batteries = batteries_per_robot * 10

    result = total_batteries
    return result

print(solution())