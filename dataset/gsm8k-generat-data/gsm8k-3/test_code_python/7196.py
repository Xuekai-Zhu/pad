def solution():
    """Aren’s flight from New York to Hawaii will take 11 hours 20 minutes.  He spends 2 hours reading, 4 hours watching two movies, 30 minutes eating his dinner, 40 minutes listening to the radio, and 1 hour 10 minutes playing games.  How many hours does he have left to take a nap?"""
    # Define the total flight time in minutes
    total_time = 11 * 60 + 20

    # Calculate the total time spent on non-nap activities in minutes
    non_nap_time = 2 * 60 + 4 * 60 + 30 + 40 + 1 * 60 + 10

    # Calculate the total nap time left in minutes
    nap_time = total_time - non_nap_time

    # Convert the nap time to hours and minutes
    nap_hours = nap_time // 60
    nap_minutes = nap_time % 60

    # Display the nap time
    result = f"{nap_hours} hours and {nap_minutes} minutes"
    return result

print(solution())