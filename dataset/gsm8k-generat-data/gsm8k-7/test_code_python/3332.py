def solution():
    total_steppings = 32
    nancy_steppings = 3
    jason_steppings = 1
    
    # Calculate the total number of times Nancy steps on her partner's feet
    nancy_total_steppings = total_steppings / 4 * 3
    
    # Calculate the total number of times Jason steps on his partner's feet
    jason_total_steppings = total_steppings / 4
    
    # Calculate the number of times Jason steps on his partner's feet
    jason_steppings = jason_total_steppings * jason_steppings
    
    result = jason_steppings
    return result

print(solution())