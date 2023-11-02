def solution():
    """Paul lives in a 5th story apartment. He makes 3 trips out from and back to his apartment throughout the day each day of a week. How many feet does he travel vertically in total over the week if each story is 10 feet tall?"""
    # Define the number of stories in Paul's building
    STORIES = 5

    # Define the height of each story
    STORY_HEIGHT = 10

    # Define the number of trips Paul makes each day
    TRIPS_PER_DAY = 3

    # Define the number of days in a week
    DAYS_PER_WEEK = 7

    # Calculate the total vertical distance traveled by Paul over the week
    total_distance = STORIES * STORY_HEIGHT * TRIPS_PER_DAY * DAYS_PER_WEEK

    # Display the total vertical distance
    result = total_distance
    return result

print(solution())