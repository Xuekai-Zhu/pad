def solution():
    """Mike began to train to play basketball every day for a tournament. One day he plays a maximum of 2 hours. After a week of training, he increased the maximum time to 3 hours. How many hours did Mike train during the first two weeks?"""
    # Define the maximum hours Mike can train per day for the first and second weeks
    MAX_HOURS_1 = 2
    MAX_HOURS_2 = 3

    # Calculate the total hours Mike can train in the first week
    total_hours_1 = MAX_HOURS_1 * 7

    # Calculate the total hours Mike can train in the second week
    total_hours_2 = MAX_HOURS_2 * 7

    # Calculate the total hours Mike trained in the first two weeks
    total_hours = total_hours_1 + total_hours_2

    # Display the total hours trained
    result = total_hours
    return result

print(solution())