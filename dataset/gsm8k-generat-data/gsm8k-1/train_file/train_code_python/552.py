def solution():
    """Emma buys 2 containers of milk every school day for lunch. She does not go to school on the weekends. How many containers of milk does she buy in 3 weeks?"""
    containers_per_day = 2
    school_days_per_week = 5
    weeks = 3
    total_containers = containers_per_day * school_days_per_week * weeks
    result = total_containers
    return result

print(solution())