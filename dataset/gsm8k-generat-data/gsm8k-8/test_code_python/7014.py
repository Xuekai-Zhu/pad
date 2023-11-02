def solution():
    # Start with 50 balloons
    balloons = 50 
    
    # Pass 1 balloon to a little girl and 12 balloons float away
    balloons -= 1
    balloons -= 12
    
    # Give 9 more away
    balloons -= 9
    
    # Take the last 11 from her coworker
    balloons += 11
    
    result = balloons
    return result

print(solution())