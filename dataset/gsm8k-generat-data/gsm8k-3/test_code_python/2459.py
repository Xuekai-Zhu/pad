def solution():
    """There are 3 workers producing chairs in a furniture factory. Each of them produces 4 chairs an hour. As a group, they produce an additional chair every 6 hours. In total, how many chairs have been produced after 6 hours?"""
    # Define the number of workers and the number of chairs produced per worker per hour
    NUM_WORKERS = 3
    CHAIRS_PER_WORKER_PER_HOUR = 4

    # Calculate the total number of chairs produced by the workers in 6 hours
    chairs_produced = NUM_WORKERS * CHAIRS_PER_WORKER_PER_HOUR * 6

    # Calculate the additional chairs produced by the group every 6 hours
    additional_chairs = 6 // 6

    # Add the additional chairs to the total number of chairs produced
    total_chairs_produced = chairs_produced + additional_chairs

    # Display the total number of chairs produced
    result = total_chairs_produced
    return result

print(solution())