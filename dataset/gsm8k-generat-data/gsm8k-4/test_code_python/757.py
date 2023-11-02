def solution():
    """Luna, the poodle, is supposed to eat 2 cups of kibble every day. But Luna's master, Mary, and her husband, Frank, sometimes feed Luna too much kibble. One day, starting with a new, 12-cup bag of kibble, Mary gave Luna 1 cup of kibble in the morning and 1 cup of kibble in the evening, But on the same day, Frank also gave Luna 1 cup of kibble in the afternoon and twice as much in the late evening as he had given Luna in the afternoon. The next morning, how many cups of kibble will Mary find remaining in the bag?"""
    # Define the amount of kibble eaten by Luna in one day
    DAILY_KIBBLE_EATEN = 2

    # Define the amount of kibble fed by Mary and Frank
    MARY_KIBBLE = 2
    FRANK_AFTERNOON_KIBBLE = 1
    FRANK_LATEEVENING_KIBBLE = FRANK_AFTERNOON_KIBBLE * 2

    # Define the amount of kibble in the bag at the start
    INITIAL_KIBBLE = 12

    # Calculate the total amount of kibble eaten by Luna in one day
    total_kibble_eaten = DAILY_KIBBLE_EATEN + MARY_KIBBLE + FRANK_AFTERNOON_KIBBLE + FRANK_LATEEVENING_KIBBLE

    # Calculate the remaining amount of kibble in the bag
    remaining_kibble = INITIAL_KIBBLE - total_kibble_eaten

    # Display the amount of kibble remaining in the bag the next morning
    result = remaining_kibble
    return result

print(solution())