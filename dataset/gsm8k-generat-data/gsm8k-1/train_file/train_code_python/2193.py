def solution():
    """The sky currently has 4 times as many cirrus clouds as cumulus clouds, and 12 times as many cumulus clouds as cumulonimbus clouds. If the sky currently has 3 cumulonimbus clouds, how many cirrus clouds are in the sky at this moment?"""
    cumulonimbus_clouds = 3
    cumulus_clouds = cumulonimbus_clouds * 12
    cirrus_clouds = cumulus_clouds * 4
    result = cirrus_clouds
    return result

print(solution())