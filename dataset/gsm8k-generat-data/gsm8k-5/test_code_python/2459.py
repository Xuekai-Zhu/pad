def solution():
    chairs_per_worker_per_hour = 4  # Each worker produces 4 chairs per hour
    num_workers = 3  # There are 3 workers in the factory

    # Calculate the total number of chairs produced by the workers in 6 hours
    total_chairs_workers = chairs_per_worker_per_hour * num_workers * 6

    # Calculate the additional chairs produced by the group in 6 hours
    additional_chairs = 6 // 1  # The group produces an additional chair every 6 hours

    # Calculate the total number of chairs produced in 6 hours
    total_chairs = total_chairs_workers + additional_chairs
    result = total_chairs
    return result

print(solution())