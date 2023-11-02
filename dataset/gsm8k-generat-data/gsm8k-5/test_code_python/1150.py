def solution():
    # Distance traveled at 30 miles per hour for 3 hours
    distance_first_leg = 30 * 3  

    # Distance traveled at 25 miles per hour for 4 hours
    distance_second_leg = 25 * 4  

    # Total distance traveled per day
    total_distance = distance_first_leg + distance_second_leg 

    # Total distance traveled in a week
    distance_weekly = total_distance * 6 # Driver delivers from Monday to Saturday

    result = distance_weekly
    return result

print(solution())