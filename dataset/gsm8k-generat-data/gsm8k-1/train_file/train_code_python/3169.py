def solution():
    """Karen is constantly trying to stop the raccoons from getting in her trash.
    The first lock she tries stalls them for 5 minutes. The next lock stalls them for 3 minutes less than three 
    times as long as the first lock. When Karen tries both locks at once, it stalled the raccoons for five times 
    as long as the second lock alone. How long is that?"""
    
    first_lock = 5
    second_lock = (3*first_lock) - 3
    combined_locks = 5*second_lock
    
    result = combined_locks
    
    return result

print(solution())