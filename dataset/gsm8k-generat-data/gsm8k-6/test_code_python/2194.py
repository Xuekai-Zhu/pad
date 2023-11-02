def solution():
    # Calculate the number of cumulus clouds in the sky
    cumulonimbus_clouds = 3
    cumulus_clouds = 12 * cumulonimbus_clouds

    # Calculate the number of cirrus clouds in the sky
    cirrus_clouds = 4 * cumulus_clouds

    result = cirrus_clouds
    return result

print(solution())