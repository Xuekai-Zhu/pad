def solution():
    """Marcos has to get across a 5 mile lake in his speedboat in 10 minutes so he can make it to work on time. How fast does he need to go in miles per hour to make it?"""
    distance = 5
    time = 10/60 #convert minutes to hours
    speed = distance/time
    result = speed
    return result

print(solution())