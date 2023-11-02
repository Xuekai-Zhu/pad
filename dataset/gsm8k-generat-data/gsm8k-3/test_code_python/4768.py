def solution():
    """John decides to get the vaccine for COVID.  He has to wait 20 minutes for the first dose.  The second dose has a wait time half as long.  How long was the total wait time?"""
    # Define the wait time for the first dose
    wait_1 = 20

    # Define the wait time for the second dose
    wait_2 = wait_1 / 2

    # Calculate the total wait time
    total_wait = wait_1 + wait_2

    # Display the total wait time
    result = total_wait
    return result

print(solution())