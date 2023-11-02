def solution():
    """Aren’s flight from New York to Hawaii will take 11 hours 20 minutes. He spends 2 hours reading, 4 hours watching two movies, 30 minutes eating his dinner, 40 minutes listening to the radio, and 1 hour 10 minutes playing games. How many hours does he have left to take a nap?"""
    # Define the total flight duration in minutes
    total_duration = 11 * 60 + 20

    # Calculate the total time spent on non-nap activities in minutes
    non_nap_duration = 2 * 60 + 4 * 60 + 30 + 40 + 1 * 60 + 10

    # Calculate the total nap time in minutes
    nap_duration = total_duration - non_nap_duration

    # Convert the nap duration from minutes to hours
    nap_hours = nap_duration / 60

    # Return the result
    result = nap_hours
    return result

print(solution())