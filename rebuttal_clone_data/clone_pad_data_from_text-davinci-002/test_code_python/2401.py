def solution():
    time_escaped = 3 #hours
    speed1 = 25 #mph
    distance1 = time_escaped * speed1 #miles
    time_running2 = 2 #hours
    speed2 = 10 #mph
    distance2 = time_running2 * speed2 #miles
    time_running3 = 0.5 #hours
    speed3 = 50 #mph
    distance3 = time_running3 * speed3 #miles
    total_distance = distance1 + distance2 + distance3
    result = total_distance
    return result

print(solution())