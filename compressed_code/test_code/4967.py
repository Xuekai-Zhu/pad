def solution():
    
    total_segments = 800
    eaten_segments = 60 + 2 * 2 * 60  
    remaining_segments = total_segments - eaten_segments
    necessary_millipedes = remaining_segments / 50
    result = necessary_millipedes
    return result

print(solution())