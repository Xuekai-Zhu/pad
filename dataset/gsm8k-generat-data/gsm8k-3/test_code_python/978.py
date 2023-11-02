def solution():
    """Stephen has 110 ants in his ant farm.  Half of the ants are worker ants, 20 percent of the worker ants are male.  How many female worker ants are there?"""
    # Define the number of total ants and the percentage of worker ants
    total_ants = 110
    worker_percentage = 0.5

    # Calculate the number of worker ants
    worker_ants = total_ants * worker_percentage

    # Calculate the number of male worker ants
    male_ants = worker_ants * 0.2

    # Calculate the number of female worker ants
    female_ants = worker_ants - male_ants

    # Display the number of female worker ants
    result = female_ants
    return result

print(solution())