def solution():
    hives = 5  # James has 5 hives
    honey_per_hive = 20  # Each hive produces 20 liters of honey
    total_honey = hives * honey_per_hive  # Total honey produced by all hives
    jars_per_liter = 2  # Each liter of honey requires 2 jars (0.5 liters per jar)
    friend_honey_share = 0.5 * total_honey  # James' friend is bringing his own jars for half the honey

    # Calculate the total number of jars James needs to buy
    total_jars = jars_per_liter * (total_honey - friend_honey_share)
    result = total_jars
    return result

print(solution())