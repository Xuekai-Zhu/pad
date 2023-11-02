def solution():
    """Four cats live in the old grey house at the end of the road.  Their names are Puffy, Scruffy, Buffy, and Juniper.  Puffy has three times more whiskers than Juniper, but half as many as Scruffy.  Buffy has the same number of whiskers as the average number of whiskers on the three other cats.  If Juniper has 12 whiskers. how many whiskers does Buffy have?"""
    # Define the number of whiskers for Juniper
    juniper_whiskers = 12

    # Calculate the number of whiskers for Puffy
    puffy_whiskers = juniper_whiskers * 3

    # Calculate the number of whiskers for Scruffy
    scruffy_whiskers = puffy_whiskers * 2

    # Calculate the average number of whiskers for the three cats excluding Buffy
    avg_whiskers = (juniper_whiskers + puffy_whiskers + scruffy_whiskers) / 3

    # Set Buffy's number of whiskers equal to the average number
    buffy_whiskers = avg_whiskers

    # Display Buffy's number of whiskers
    result = buffy_whiskers
    return result

print(solution())