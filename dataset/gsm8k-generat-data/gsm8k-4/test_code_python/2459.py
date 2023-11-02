def solution():
    """There are 3 workers producing chairs in a furniture factory. Each of them produces 4 chairs an hour. As a group, they produce an additional chair every 6 hours. In total, how many chairs have been produced after 6 hours?"""
    # Define the number of workers and the chairs produced per hour per worker
    NUM_WORKERS = 3
    CHAIRS_PER_HOUR_PER_WORKER = 4

    # Calculate the chairs produced by the workers after 6 hours
    chairs_produced_before_bonus = NUM_WORKERS * CHAIRS_PER_HOUR_PER_WORKER * 6

    # Calculate the additional chair produced after 6 hours
    additional_chair_produced = 1

    # Calculate the total number of chairs produced after 6 hours
    total_chairs_produced = chairs_produced_before_bonus + additional_chair_produced

    # Return the result
    result = total_chairs_produced
    return result

print(solution())