def solution():
    """At the beginning of the day, Principal Kumar instructed Harold to raise the flag up the flagpole. The flagpole is 60 feet long, and when fully raised, the flag sits on the very top of the flagpole. Later that morning, Vice-principal Zizi instructed Harold to lower the flag to half-mast. So, Harold lowered the flag halfway down the pole. Later, Principal Kumar told Harold to raise the flag to the top of the pole once again, and Harold did just that. At the end of the day, Vice-principal Zizi instructed Harold to completely lower the flag, take it off of the pole, and put it away for the evening. Over the course of the day, how far, in feet, had the flag moved up and down the pole?"""
    # Define the length of the flagpole and the starting position of the flag
    FLAGPOLE_LENGTH = 60
    FLAG_START_POSITION = 0

    # Calculate the distance moved from raising the flag to the top of the pole
    distance_raised = FLAGPOLE_LENGTH - FLAG_START_POSITION

    # Calculate the distance moved from lowering the flag to half-mast and then raising it to the top again
    distance_halfmast = FLAGPOLE_LENGTH / 2

    # Calculate the distance moved from lowering the flag from the top to taking it off the pole
    distance_lowered = FLAGPOLE_LENGTH - FLAG_START_POSITION

    # Calculate the total distance moved by the flag
    total_distance = distance_raised + distance_halfmast + distance_raised + distance_lowered

    # Return the result
    result = total_distance
    return result

print(solution())