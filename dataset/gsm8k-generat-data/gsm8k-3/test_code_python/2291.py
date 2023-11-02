def solution():
    """Trish likes to go for walks every day.  One day, she goes on a 1-mile walk.  
    Every subsequent day, she doubles the distance she walked the previous day.  
    On what day does she walk more than 10 times further than she did on the first day?"""
    # Initialize variables
    distance_walked = 1
    day = 1

    # Loop until distance walked is more than 10 times the initial distance
    while distance_walked <= 10:
        day += 1
        distance_walked *= 2

    # Display the day
    result = day
    return result

print(solution())