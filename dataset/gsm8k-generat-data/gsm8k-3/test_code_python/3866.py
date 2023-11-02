def solution():
    """A bicycle shop owner adds 3 bikes to her stock every week. After 1 month, she had sold 18 bikes but still had 45 bikes in stock. How many bikes did she have originally?"""
    # Define the number of bikes added to the stock every week
    bikes_added_per_week = 3

    # Calculate the number of bikes she had after 1 week
    bikes_after_1_week = 45 + 18 + 3*4

    # Calculate the number of bikes she had originally
    bikes_orig = bikes_after_1_week - 3*4

    # Display the number of bikes she had originally
    result = bikes_orig
    return result

print(solution())