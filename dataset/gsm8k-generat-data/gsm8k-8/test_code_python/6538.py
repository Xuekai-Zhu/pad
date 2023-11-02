def solution():
    # Total length of the path including the bridge
    total_length = 900
    
    # Length of the path without the bridge
    path_length = total_length - 42
    
    # Number of fence poles needed for the entire length
    fence_poles = path_length / 6
    
    # Number of fence poles on each side of the path
    poles_per_side = fence_poles / 2
    
    result = poles_per_side
    return result

print(solution())