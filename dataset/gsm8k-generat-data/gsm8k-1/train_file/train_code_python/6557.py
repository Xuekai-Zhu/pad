def solution():
    """It takes 20 minutes for John to go to the bathroom 8 times. How long would it take to go 6 times?"""
    num_times_initial = 8
    time_initial = 20
    num_times_new = 6
    time_new = (num_times_new * time_initial) / num_times_initial
    result = time_new
    return result

print(solution())