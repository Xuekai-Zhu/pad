def solution():
    # Define the ratio of cirrus clouds to cumulus clouds
    cirrus_to_cumulus_ratio = 4

    # Define the ratio of cumulus clouds to cumulonimbus clouds
    cumulus_to_cumulonimbus_ratio = 12

    # Calculate the total number of cumulus clouds
    total_cumulus_clouds = 12 * 3

    # Calculate the total number of cirrus clouds
    total_cirrus_clouds = 4 * total_cumulus_clouds

    result = total_cirrus_clouds
    return result

print(solution())