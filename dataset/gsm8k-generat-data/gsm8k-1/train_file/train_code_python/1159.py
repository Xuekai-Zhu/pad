def solution():
    """On a normal day, Julia can run a mile in 10 minutes. However, today she decided to wear her new shoes to run. They were uncomfortable and slowed her mile down to 13 minutes. How much longer would it take Julia to run 5 miles in her new shoes than if she wore her old ones?"""
    old_time_per_mile = 10
    new_time_per_mile = 13
    distance = 5
    time_difference_per_mile = new_time_per_mile - old_time_per_mile
    extra_time = time_difference_per_mile * distance
    result = extra_time
    return result

print(solution())