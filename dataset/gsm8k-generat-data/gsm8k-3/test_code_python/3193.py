def solution():
    """It takes 40 minutes to freeze ice cubes and 3 minutes per smoothie to turn them into smoothies once they're frozen. How long does it take to make 5 smoothies?"""
    # Define the time to freeze ice cubes and to turn them into smoothies
    FREEZING_TIME = 40
    BLENDING_TIME_PER_SMOOTHIE = 3

    # Calculate the total time to make 5 smoothies
    total_time = FREEZING_TIME + (BLENDING_TIME_PER_SMOOTHIE * 5)

    # Display the total time
    result = total_time
    return result

print(solution())