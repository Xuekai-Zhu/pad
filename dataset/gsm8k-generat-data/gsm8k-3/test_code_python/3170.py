def solution():
    """Karen is constantly trying to stop the raccoons from getting in her trash. The first lock she tries stalls them for 5 minutes. The next lock stalls them for 3 minutes less than three times as long as the first lock. When Karen tries both locks at once, it stalled the raccoons for five times as long as the second lock alone. How long is that?"""
    
    # Define the time each lock stalls the raccoons
    lock1_time = 5
    lock2_time = 3*(lock1_time) - 3
    
    # Calculate the total time when both locks are used
    total_time = 5*(lock2_time)

    # Display the total time
    result = total_time
    return result

print(solution())