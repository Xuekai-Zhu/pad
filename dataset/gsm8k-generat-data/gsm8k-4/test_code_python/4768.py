def solution():
    """John decides to get the vaccine for COVID. He has to wait 20 minutes for the first dose. The second dose has a wait time half as long. How long was the total wait time?"""
    # Calculate the total wait time for both doses
    total_wait_time = 20 + (20/2)

    # return the result
    result = total_wait_time
    return result

print(solution())