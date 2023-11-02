def solution():
    """Bob runs 6 miles per hour. His friend Jim runs at 9 miles per hour. If Bob has a 1 mile head-start, how many minutes will it take before Jim catches him?"""
    bob_speed = 6/60 # miles per minute
    jim_speed = 9/60 # miles per minute
    head_start = 1 # mile
    time_to_catch_up = head_start / (jim_speed - bob_speed) # in minutes
    
    result = time_to_catch_up
    return result

print(solution())