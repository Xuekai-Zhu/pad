def solution():
    """Walter fell from the eighth platform of some scaffolding and fell past David after falling 4 meters. If he fell for an additional three more times that depth before hitting the ground, and the platforms are evenly spaced out in height, what platform was David on?"""
    # Define the height of each platform
    PLATFORM_HEIGHT = 4

    # Define the distance Walter fell before passing David
    walter_fall = 8 * PLATFORM_HEIGHT - 4

    # Define the total distance Walter fell
    total_fall = walter_fall + 3 * PLATFORM_HEIGHT

    # Calculate the number of platforms David was on
    david_platforms = total_fall // PLATFORM_HEIGHT

    # Display the platform number David was on
    result = david_platforms
    return result

print(solution())