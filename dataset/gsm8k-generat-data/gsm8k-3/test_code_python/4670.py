def solution():
    """At the beginning of the day, Principal Kumar instructed Harold to raise the flag up the flagpole.  The flagpole is 60 feet long, and when fully raised, the flag sits on the very top of the flagpole.  Later that morning, Vice-principal Zizi instructed Harold to lower the flag to half-mast.  So, Harold lowered the flag halfway down the pole.   Later, Principal Kumar told Harold to raise the flag to the top of the pole once again, and Harold did just that.  At the end of the day, Vice-principal Zizi instructed Harold to completely lower the flag, take it off of the pole, and put it away for the evening.  Over the course of the day, how far, in feet, had the flag moved up and down the pole?"""
    # Define the length of the flagpole
    FLAGPOLE_LENGTH = 60

    # Calculate the distance the flag moves when raised to the top
    distance_1 = FLAGPOLE_LENGTH

    # Calculate the distance the flag moves when lowered halfway
    distance_2 = FLAGPOLE_LENGTH/2

    # Calculate the distance the flag moves when raised to the top again
    distance_3 = FLAGPOLE_LENGTH/2

    # Calculate the distance the flag moves when lowered and taken off
    distance_4 = FLAGPOLE_LENGTH/2

    # Calculate the total distance the flag moves over the course of the day
    total_distance = distance_1 + distance_2 + distance_3 + distance_4

    # Display the total distance
    result = total_distance
    return result

print(solution())