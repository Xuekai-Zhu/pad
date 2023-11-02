def solution(): 
    # Calculate Madison's spitting distance and Ryan's spitting distance
    madison_distance = 30 * 1.2  # Madison can spit 20% farther than Billy
    ryan_distance = madison_distance * 0.5  # Ryan can spit 50% shorter than Madison
    
    result = ryan_distance
    return result

print(solution())