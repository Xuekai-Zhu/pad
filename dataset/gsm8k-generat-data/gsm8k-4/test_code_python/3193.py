def solution():
    """It takes 40 minutes to freeze ice cubes and 3 minutes per smoothie to turn them into smoothies once they're frozen. How long does it take to make 5 smoothies?"""
    # Define the time to freeze ice cubes and make one smoothie
    freeze_time = 40
    smoothie_time = 3

    # Calculate the total time to make 5 smoothies
    total_time = freeze_time + (5 * smoothie_time)

    result = total_time
    return result

print(solution())