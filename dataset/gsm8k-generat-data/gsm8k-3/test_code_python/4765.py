def solution():
    """Javier spends 30 minutes outlining his speech, 28 more minutes writing than outlining, and half as much time practicing as writing. How much time does he spend on his speech in total?"""
    # Define the time Javier spends outlining his speech
    outline_time = 30

    # Define the time Javier spends writing his speech
    writing_time = outline_time + 28

    # Define the time Javier spends practicing his speech
    practice_time = writing_time / 2

    # Calculate the total time Javier spends on his speech
    total_time = outline_time + writing_time + practice_time

    # Display the total time
    result = total_time
    return result

print(solution())