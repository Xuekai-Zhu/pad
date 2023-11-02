def solution():
    """Paul lives in a 5th story apartment. He makes 3 trips out from and back to his apartment throughout the day each day of a week. How many feet does he travel vertically in total over the week if each story is 10 feet tall?"""
    # Define the number of stories in the building and the distance in feet per story
    STORIES = 5
    FEET_PER_STORY = 10

    # Define the number of trips per day and the number of days
    TRIPS_PER_DAY = 3
    DAYS = 7

    # Calculate the total vertical distance traveled in feet
    vertical_distance = STORIES * FEET_PER_STORY * TRIPS_PER_DAY * DAYS

    # return the result
    result = vertical_distance
    return result

print(solution())