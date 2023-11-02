def solution():
    # Calculate the total amount of honey James has
    total_honey = 5 * 20  # 100 liters

    # Calculate the number of jars needed for James's half of the honey
    jars_needed = total_honey / 0.5

    # Calculate the number of jars needed for his friend's half of the honey
    friend_jars = jars_needed / 2

    # Calculate the total number of jars needed
    total_jars = jars_needed + friend_jars

    result = total_jars
    return result

print(solution())