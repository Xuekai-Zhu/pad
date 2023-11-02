def solution():
    """Kenny played basketball last week. He ran for twice as long as he played basketball, and he practiced on the trumpet for twice as long as he ran. If he practiced on the trumpet for 40 hours, how many hours did Kenny play basketball last week?"""
    # Define the time Kenny spent practicing on the trumpet
    trumpet_time = 40

    # Calculate the time Kenny spent running
    running_time = trumpet_time / 2

    # Calculate the time Kenny spent playing basketball
    basketball_time = running_time / 2

    result = basketball_time
    return result

print(solution())