def solution():
    """If 2 machines in a factory make 10 cell phones each minute, how many machines would it take to make 50 cell phones a minute?"""
    # Define the number of machines and cell phones per minute
    machines = 2
    cellphones_per_minute = 10

    # Calculate the number of machines needed to produce 50 cell phones per minute
    machines_needed = (50 / cellphones_per_minute) / machines

    # Round up to the nearest integer
    machines_needed = int(machines_needed) + 1

    result = machines_needed
    return result

print(solution())