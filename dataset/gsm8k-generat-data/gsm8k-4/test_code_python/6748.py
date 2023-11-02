def solution():
    """Four cats live in the old grey house at the end of the road. Their names are Puffy, Scruffy, Buffy, and Juniper. Puffy has three times more whiskers than Juniper, but half as many as Scruffy. Buffy has the same number of whiskers as the average number of whiskers on the three other cats. If Juniper has 12 whiskers, how many whiskers does Buffy have?"""
    # Define the number of whiskers on Juniper
    juniper_whiskers = 12

    # Calculate the number of whiskers on Puffy and Scruffy
    puffy_whiskers = juniper_whiskers * 3
    scruffy_whiskers = puffy_whiskers * 2

    # Calculate the total number of whiskers on the three cats without Buffy
    total_whiskers = juniper_whiskers + puffy_whiskers + scruffy_whiskers

    # Calculate the number of whiskers on Buffy
    buffy_whiskers = total_whiskers / 3

    # Return the result
    result = buffy_whiskers
    return result

print(solution())