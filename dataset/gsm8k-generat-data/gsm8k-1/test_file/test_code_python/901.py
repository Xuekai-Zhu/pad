def solution():
    """Harold sleeps for 10 hours a night. He works 2 hours less than he sleeps and he walks his dog for an hour each day. How much free time does Harold have left in his day?"""
    sleep_hours = 10
    work_hours = sleep_hours - 2
    dog_walk_hours = 1
    total_hours = 24
    free_hours = total_hours - sleep_hours - work_hours - dog_walk_hours
    result = free_hours
    return result

print(solution())