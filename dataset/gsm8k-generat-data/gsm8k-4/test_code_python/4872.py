def solution():
    """Jill is the hairdresser for the school's dance team and has to braid 8 dancers' hair. If each dancer has five braids and each braid takes 30 seconds, how many minutes will it take to braid all the dancers' hair?"""
    # Define the number of dancers and braids per dancer
    num_dancers = 8
    braids_per_dancer = 5

    # Calculate the total number of braids needed to be done
    total_braids = num_dancers * braids_per_dancer

    # Calculate the total time in seconds needed to do all braids
    total_time_sec = total_braids * 30

    # Convert the time to minutes
    total_time_min = total_time_sec / 60

    # Round the result to the nearest minute
    result = round(total_time_min)
    return result

print(solution())