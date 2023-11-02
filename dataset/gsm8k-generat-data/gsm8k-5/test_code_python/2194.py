def solution():
    cumulonimbus_clouds = 3 # There are 3 cumulonimbus clouds
    cumulus_clouds = cumulonimbus_clouds * 12 # There are 12 times as many cumulus clouds as cumulonimbus clouds
    cirrus_clouds = cumulus_clouds * 4 # There are 4 times as many cirrus clouds as cumulus clouds
    result = cirrus_clouds
    return result

print(solution())