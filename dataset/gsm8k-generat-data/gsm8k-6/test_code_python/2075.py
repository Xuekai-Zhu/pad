def solution():
    # Let's assume the son's speed is x m/s
    son_speed = x
    # Then, the father's speed is 3x m/s
    father_speed = 3*x
    
    # We can set up an equation using time and distance
    # The distance they cover when they meet is 16m
    # We want to find out the distance from the father's end
    # Let t be the time it takes for them to meet
    
    # distance covered by the son in time t
    son_distance = t * son_speed
    # distance covered by the father in time t
    father_distance = t * father_speed
    
    # At the meeting point, the sum of their distances is 16m
    son_distance + father_distance = 16
    
    # We can solve for t
    t = 16 / (son_speed + father_speed)
    
    # Then, we can find out the distance from the father's end
    distance_from_father_end = father_speed * t
    
    result = distance_from_father_end
    return result

print(solution())