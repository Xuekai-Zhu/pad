def solution():
    # Calculate the total liters of honey produced by James' hives
    total_honey = 5 * 20  # 5 hives each producing 20 liters of honey

    # Calculate the total number of jars needed to hold all the honey
    total_jars = total_honey / 0.5  # each jar can hold 0.5 liters of honey

    # Halve the number of jars needed since James' friend is bringing their own jars for half the honey
    total_jars = total_jars / 2

    result = total_jars
    return result

print(solution())