def solution():
    
    
    balloons_before = 12
    balloons_after = 50
    balloons_blow_up_by_andy = balloons_after - balloons_before
    
    
    balloons_per_blow_up = 2
    total_blow_ups = balloons_blow_up_by_andy / balloons_per_blow_up
    
    
    minutes_per_blow_up = 5
    total_minutes = total_blow_ups * minutes_per_blow_up
    
    result = total_minutes
    return result

print(solution())