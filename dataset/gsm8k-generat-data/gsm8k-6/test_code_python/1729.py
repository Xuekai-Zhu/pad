def solution():
    # Calculate the total number of insects in Calvin's collection
    roaches = 12
    scorpions = 3
    crickets = roaches / 2
    caterpillars = 2 * scorpions
    total_insects = roaches + scorpions + crickets + caterpillars
    result = total_insects
    return result

print(solution())