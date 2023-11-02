def solution():
    """Four cats live in the old grey house at the end of the road. Their names are Puffy, Scruffy, Buffy, and Juniper. Puffy has three times more whiskers than Juniper, but half as many as Scruffy. Buffy has the same number of whiskers as the average number of whiskers on the three other cats. If Juniper has 12 whiskers, how many whiskers does Buffy have?"""
    juniper_whiskers = 12
    puffy_whiskers = 3 * juniper_whiskers
    scruffy_whiskers = 2 * puffy_whiskers
    total_whiskers = juniper_whiskers + puffy_whiskers + scruffy_whiskers
    buffy_whiskers = total_whiskers / 3
    result = buffy_whiskers
    return result

print(solution())