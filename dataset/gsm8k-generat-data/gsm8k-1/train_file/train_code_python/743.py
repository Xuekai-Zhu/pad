def solution():
    """Yolanda leaves home for work at 7:00 AM, riding her bike at 20 miles per hour. 15 minutes after she leaves, her husband realizes that she forgot her lunch, and jumps in the car to bring it to her. If he drives at 40 miles per hour and follows the exact same route as Yolanda, how many minutes will it take him to catch her?"""
    yolanda_speed = 20 # in mph
    husband_speed = 40 # in mph
    time_difference = 0.25 #15 min = 0.25 hours
    yolanda_distance = yolanda_speed * time_difference #in miles
    relative_speed = husband_speed - yolanda_speed
    time_to_catch = yolanda_distance / relative_speed #in hours
    time_to_catch_min = round(time_to_catch * 60) #in minutes
    
    return time_to_catch_min

print(solution())