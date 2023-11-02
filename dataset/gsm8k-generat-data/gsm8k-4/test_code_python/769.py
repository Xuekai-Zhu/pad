def solution():
    """Bill put his french fries in the oven after it finished heating. The recommended time was 5 minutes for them to be fully cooked. He put them in for 45 seconds. How many seconds remained?"""
    # Define the recommended cooking time and the actual cooking time
    recommended_cooking_time = 5 * 60  # in seconds
    actual_cooking_time = 45  # in seconds

    # Calculate the remaining cooking time
    remaining_time = recommended_cooking_time - actual_cooking_time

    # Return the result
    result = remaining_time
    return result

print(solution())