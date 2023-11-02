def solution():
    """Mike began to train to play basketball every day for a tournament. One day he plays a maximum of 2 hours. After a week of training, he increased the maximum time to 3 hours. How many hours did Mike train during the first two weeks?"""
    # Define the maximum time Mike played on the first day
    day_one_max = 2

    # Define the total number of days in two weeks
    days = 14

    # Define the number of days in the first week
    first_week_days = 7

    # Define the maximum time Mike played in the second week
    second_week_max = 3

    # Calculate the total time Mike trained during the first week
    first_week_time = day_one_max * first_week_days

    # Calculate the total time Mike trained during the second week
    second_week_time = second_week_max * (days - first_week_days)

    # Calculate the total time Mike trained during the first two weeks
    total_time = first_week_time + second_week_time

    # Return the result
    result = total_time
    return result

print(solution())