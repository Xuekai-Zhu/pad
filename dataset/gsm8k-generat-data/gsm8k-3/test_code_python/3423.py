def solution():
    """There are 14 chickens in the coop, and twice that many in the run. There is 4 less than double the number of chickens free ranging as in the run.  How many chickens are free ranging?"""
    # Define the number of chickens in the coop
    coop_chickens = 14

    # Calculate the number of chickens in the run
    run_chickens = coop_chickens * 2

    # Calculate the number of free ranging chickens
    free_chickens = (2 * run_chickens) - 4

    # Display the number of free ranging chickens
    result = free_chickens
    return result

print(solution())