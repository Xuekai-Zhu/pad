def solution():
    """Paul, Amoura, and Ingrid were to go to a friend's party planned to start at 8:00 a.m. Paul arrived at 8:25. Amoura arrived 30 minutes later than Paul, and Ingrid was three times later than Amoura. How late, in minutes, was Ingrid to the party?"""
    # Define the start time of the party and the arrival time of Paul
    party_start_time = 8 * 60  # in minutes
    paul_arrival_time = 8 * 60 + 25  # in minutes

    # Calculate the arrival time of Amoura and Ingrid
    amoura_arrival_time = paul_arrival_time + 30
    ingrid_arrival_time = amoura_arrival_time + 3*(amoura_arrival_time - paul_arrival_time)

    # Calculate the delay of Ingrid to the party
    delay = ingrid_arrival_time - party_start_time

    result = delay
    return result

print(solution())