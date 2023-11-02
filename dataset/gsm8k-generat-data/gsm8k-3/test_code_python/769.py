def solution():
    """Bill put his french fries in the oven after it finished heating.  The recommended time was 5 minutes for them to be fully cooked.  He put them in for 45 seconds.  How many seconds remained?"""
    # Define the recommended cooking time in seconds
    recommended_time = 5 * 60

    # Define the time Bill cooked his fries in seconds
    actual_time = 45

    # Calculate the remaining cooking time in seconds
    remaining_time = recommended_time - actual_time

    # Display the remaining cooking time in seconds
    result = remaining_time
    return result

print(solution())