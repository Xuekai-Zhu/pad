def solution():
    """The sky currently has 4 times as many cirrus clouds as cumulus clouds, and 12 times as many cumulus clouds as cumulonimbus clouds.  If the sky currently has 3 cumulonimbus clouds, how many cirrus clouds are in the sky at this moment?"""
    # Define the number of cumulonimbus clouds
    CUMULONIMBUS_CLOUDS = 3

    # Calculate the number of cumulus clouds
    cumulus_clouds = CUMULONIMBUS_CLOUDS * 12

    # Calculate the number of cirrus clouds
    cirrus_clouds = cumulus_clouds * 4

    # Display the number of cirrus clouds
    result = cirrus_clouds
    return result

print(solution())