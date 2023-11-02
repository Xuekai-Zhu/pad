def solution():
    """Gretchen read that you should spend 10 minutes walking for every 90 minutes you spend sitting. If Gretchen spends 6 hours working at her desk, how long will she spend walking?"""
    # Define the ratio of walking time to sitting time
    WALKING_RATIO = 10 / 90

    # Define the time Gretchen spends at her desk in minutes
    desk_time = 6 * 60

    # Calculate the time Gretchen should spend walking
    walking_time = desk_time * WALKING_RATIO

    # Display the time Gretchen should spend walking
    result = walking_time
    return result

print(solution())