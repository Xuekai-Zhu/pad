def solution():
    painting_time = 8
    counter_time = 3 * painting_time
    lawn_time = 6
    hourly_rate = 15

    # Calculate total time spent on the job
    total_time = painting_time + counter_time + lawn_time

    # Calculate total cost of the job
    total_cost = total_time * hourly_rate
    result = total_cost
    return result

print(solution())