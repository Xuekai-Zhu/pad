def solution():
    """Jill is the hairdresser for the school's dance team and has to braid 8 dancers' hair. If each dancer has five braids and each braid takes 30 seconds, how many minutes will it take to braid all the dancers' hair?"""
    # Define the number of dancers and braids per dancer
    num_dancers = 8
    braids_per_dancer = 5

    # Define the time it takes to braid one braid
    braid_time = 30 # in seconds

    # Calculate the total time it will take to braid all the dancers' hair
    total_time = num_dancers * braids_per_dancer * braid_time

    # Convert the total time from seconds to minutes
    total_time_minutes = total_time / 60

    # Display the total time in minutes
    result = total_time_minutes
    return result

print(solution())