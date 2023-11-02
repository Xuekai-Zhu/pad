def solution():
    """Gunther needs to clean his apartment. It takes him 45 minutes to vacuum the carpets, 60 minutes to dust the furniture, 30 minutes to mop the floors in his kitchen, and 5 minutes to brush each cat, and he has three cats. If he has 3 hours of free time available, and he uses this time to clean his apartment, how many minutes of free time will he have left after he cleans the apartment?"""
    total_time = (45 + 60 + 30 + (5 * 3))  # Total time in minutes
    free_time = 3 * 60  # 3 hours of free time in minutes
    remaining_time = free_time - total_time
    result = remaining_time
    return result

print(solution())