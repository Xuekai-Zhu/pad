def solution():
    """In preparation for the upcoming Olympics, Rita's swimming coach requires her to swim a total of 1,500 hours.
    Rita has already completed 50 hours of backstroke, 9 hours of breaststroke, and 121 hours of butterfly, but she is unhappy with her inconsistency.
    She has therefore decided to dedicate 220 hours every month practicing freestyle and sidestroke.
    How many months does Rita have to fulfill her coach’s requirements?"""
    
    total_hours = 1500
    completed_hours = 50 + 9 + 121
    remaining_hours = total_hours - completed_hours
    monthly_hours = 220
    months_needed = remaining_hours / monthly_hours
    result = months_needed
    
    return result

print(solution())