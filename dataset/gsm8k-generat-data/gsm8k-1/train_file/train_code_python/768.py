def solution():
    """Bill put his french fries in the oven after it finished heating. The recommended time was 5 minutes for them to be fully cooked. He put them in for 45 seconds. How many seconds remained?"""
    recommended_time = 5 * 60
    actual_time = 45
    time_remaining = recommended_time - actual_time
    result = time_remaining
    return result

print(solution())