def solution():
    """Troy's home is 75 meters away from school while Emily's home is 98 meters away from school. Troy and Emily walk to school and back home every day. How much farther does Emily walk to school and back in five days?"""
    # Define the distance from Troy's home to school and back
    troy_distance = 75 * 2

    # Define the distance from Emily's home to school and back
    emily_distance = 98 * 2

    # Calculate the difference in distance walked by Emily and Troy in a day
    daily_difference = emily_distance - troy_distance

    # Calculate the total difference in distance walked by Emily and Troy in five days
    total_difference = daily_difference * 5

    result = total_difference
    return result

print(solution())