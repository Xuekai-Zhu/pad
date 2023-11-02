def solution():
    """Fernanda purchased six audiobooks from Audible to listen to from her audible app. If each audiobook was 30 hours long and she listened to 2 hours of an audiobook each day, calculate the total time it took her to finish the six audiobooks?"""
    # Define the length of each audiobook and the time Fernanda listens per day
    AUDIOBOOK_LENGTH = 30
    DAILY_LISTENING_TIME = 2

    # Calculate the total time it takes Fernanda to finish all the audiobooks
    total_time = AUDIOBOOK_LENGTH * 6 / DAILY_LISTENING_TIME

    # Display the total time
    result = total_time
    return result

print(solution())