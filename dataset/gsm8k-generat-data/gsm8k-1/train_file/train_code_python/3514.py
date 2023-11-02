def solution():
    """Hugo can fold a small box in 3 seconds and a medium one in twice that time. Tom can fold both the small and medium boxes in 4 seconds. 
    If Hugo and Tom want to leave as early as possible, how long (in seconds) will it take them to fold 2400 small boxes and 1800 medium boxes?"""
    
    # Time it takes Hugo to fold a small box
    hugo_small_time = 3
    
    # Time it takes Hugo to fold a medium box
    hugo_medium_time = 2 * hugo_small_time
    
    # Time it takes Tom to fold a small or medium box
    tom_time = 4
    
    # Total time it takes Hugo to fold all small boxes
    total_hugo_small_time = hugo_small_time * 2400
    
    # Total time it takes Hugo to fold all medium boxes
    total_hugo_medium_time = hugo_medium_time * 1800
    
    # Total time it takes Tom to fold all boxes
    total_tom_time = tom_time * (2400 + 1800)
    
    # Time it takes both Hugo and Tom to fold all boxes
    total_time = max(total_hugo_small_time, total_hugo_medium_time, total_tom_time)
    
    return total_time

print(solution())