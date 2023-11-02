def solution():
    """If 2 machines in a factory make 10 cell phones each minute, how many machines would it take to make 50 cell phones a minute?"""
    # Define the number of phones made per minute by one machine
    PHONES_PER_MIN = 10

    # Define the desired number of phones made per minute
    DESIRED_PHONES_PER_MIN = 50

    # Calculate the number of machines needed to make the desired number of phones per minute
    machines_needed = DESIRED_PHONES_PER_MIN / PHONES_PER_MIN

    # Round up to the nearest whole number of machines
    machines_needed = math.ceil(machines_needed)

    # Display the number of machines needed
    result = machines_needed
    return result

print(solution())