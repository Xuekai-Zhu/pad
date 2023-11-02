def solution():
    num_hives = 5
    honey_per_hive = 20
    jar_capacity = 0.5
    friend_jars = True

    # Calculate the total amount of honey James has
    total_honey = num_hives * honey_per_hive

    # Calculate the total number of jars James needs
    if friend_jars:
        total_jars = total_honey / jar_capacity / 1.5
    else:
        total_jars = total_honey / jar_capacity

    result = total_jars
    return result

print(solution())