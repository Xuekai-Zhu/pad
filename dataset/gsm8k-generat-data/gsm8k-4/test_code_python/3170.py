def solution():
    """Karen is constantly trying to stop the raccoons from getting in her trash. The first lock she tries stalls them for 5 minutes. The next lock stalls them for 3 minutes less than three times as long as the first lock. When Karen tries both locks at once, it stalled the raccoons for five times as long as the second lock alone. How long is that?"""
    # Define the time stalled by the first lock
    lock1_time = 5

    # Define the time stalled by the second lock
    lock2_time = (3 * lock1_time) - 3

    # Define the time stalled by both locks together
    locks_together_time = 5 * lock2_time

    result = locks_together_time
    return result

print(solution())