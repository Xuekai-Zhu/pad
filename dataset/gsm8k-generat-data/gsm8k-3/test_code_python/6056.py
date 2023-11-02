def solution():
    """Paul, Amoura, and Ingrid were to go to a friend's party planned to start at 8:00 a.m. Paul arrived at 8:25. Amoura arrived 30 minutes later than Paul, and Ingrid was three times later than Amoura. How late, in minutes, was Ingrid to the party?"""
    # Define the start time of the party
    PARTY_START_TIME = 8 * 60 # convert 8:00 a.m. to minutes

    # Define the arrival times of Paul, Amoura, and Ingrid
    paul_arrival_time = PARTY_START_TIME + 25 # Paul arrived at 8:25
    amoura_arrival_time = paul_arrival_time + 30 # Amoura arrived 30 minutes later than Paul
    ingrid_arrival_time = amoura_arrival_time + 3 * 30 # Ingrid was three times later than Amoura

    # Calculate the lateness of Ingrid
    ingrid_lateness = ingrid_arrival_time - PARTY_START_TIME

    # Display the lateness of Ingrid
    result = ingrid_lateness
    return result

print(solution())