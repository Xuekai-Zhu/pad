def solution():
    """Javier spends 30 minutes outlining his speech, 28 more minutes writing than outlining, and half as much time practicing as writing. How much time does he spend on his speech in total?"""
    # Define the time spent outlining the speech
    outlining_time = 30

    # Define the time spent writing the speech
    writing_time = outlining_time + 28

    # Define the time spent practicing the speech
    practicing_time = writing_time / 2

    # Calculate the total time spent on the speech
    total_time = outlining_time + writing_time + practicing_time

    # return the result
    result = total_time
    return result

print(solution())