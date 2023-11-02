def solution():
    """The sky currently has 4 times as many cirrus clouds as cumulus clouds, and 12 times as many cumulus clouds as cumulonimbus clouds. If the sky currently has 3 cumulonimbus clouds, how many cirrus clouds are in the sky at this moment?"""
    # Define the initial number of cumulonimbus clouds
    cumulonimbus_clouds = 3

    # Calculate the number of cumulus clouds
    cumulus_clouds = cumulonimbus_clouds * 12

    # Calculate the number of cirrus clouds
    cirrus_clouds = cumulus_clouds * 4

    # Return the result
    result = cirrus_clouds
    return result

print(solution())