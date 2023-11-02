def solution():
    """Fernanda purchased six audiobooks from Audible to listen to from her audible app. If each audiobook was 30 hours long and she listened to 2 hours of an audiobook each day, calculate the total time it took her to finish the six audiobooks?"""
    # Define the length of each audiobook in hours
    audiobook_length = 30

    # Define the number of audiobooks purchased
    num_audiobooks = 6

    # Define the number of hours listened to each day
    daily_listening_hours = 2

    # Calculate the total time it would take to finish one audiobook
    total_hours_per_audiobook = audiobook_length / daily_listening_hours

    # Calculate the total time it would take to finish all audiobooks
    total_hours_all_audiobooks = total_hours_per_audiobook * num_audiobooks

    # Return the result in days
    result = total_hours_all_audiobooks / 24
    return result

print(solution())