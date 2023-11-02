def solution():
    """On a normal day, Julia can run a mile in 10 minutes. However, today she decided to wear her new shoes to run. They were uncomfortable and slowed her mile down to 13 minutes. How much longer would it take Julia to run 5 miles in her new shoes than if she wore her old ones?"""
    old_time = 10
    new_time = 13
    distance = 5
    time_difference = new_time - old_time
    extra_time = time_difference * distance
    result = extra_time
    return result

print(solution())