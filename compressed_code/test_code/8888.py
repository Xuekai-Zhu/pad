def solution():
    
    j_time_awake = (2/3)*24
    j_time_outside = (1/2)*j_time_awake
    j_time_inside = j_time_awake - j_time_outside
    r_time_awake = (3/4)*24
    r_time_outside = (1/3)*r_time_awake
    r_time_inside = r_time_awake - r_time_outside
    avg_time_inside = (j_time_inside + r_time_inside) / 2
    result = avg_time_inside
    return result

print(solution())