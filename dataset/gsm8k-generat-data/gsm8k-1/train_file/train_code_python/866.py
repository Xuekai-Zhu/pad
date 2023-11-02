def solution():
    """Bob runs 6 miles per hour. His friend Jim runs at 9 miles per hour. If Bob has a 1 mile head-start, how many minutes will it take before Jim catches him?"""
    bob_speed = 6
    jim_speed = 9
    head_start = 1
    
    # Calculate the time it takes for Jim to catch up to Bob
    time = head_start / (jim_speed - bob_speed) * 60
    
    result = time
    return result

print(solution())