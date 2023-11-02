def solution():
    """Walter fell from the eighth platform of some scaffolding and fell past David after falling 4 meters. If he fell for an additional three more times that depth before hitting the ground, and the platforms are evenly spaced out in height, what platform was David on?"""
    # Define the total number of platforms
    total_platforms = 8

    # Define the depth Walter fell in meters
    depth = 4

    # Calculate the total distance Walter fell
    total_distance = depth * 4

    # Calculate the height of each platform
    platform_height = total_distance / total_platforms

    # Calculate the platform number David was on
    david_platform = (total_distance - depth) // platform_height

    result = david_platform
    return result

print(solution())