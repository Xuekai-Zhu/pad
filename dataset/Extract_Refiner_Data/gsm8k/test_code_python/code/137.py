def solution():
    
    # Define the number of bees and the ratios of workers to baby bees
    bees = 700
    worker_to_baby_ratio = 2

    # Calculate the number of babies and queens
    babies = bees * 2
    queens = babies / 2

    # Calculate the number of workers
    workers = babies * worker_to_baby_ratio + queens * worker_to_baby_ratio

    # Display the number of workers
    result = workers
    return result

print(solution())