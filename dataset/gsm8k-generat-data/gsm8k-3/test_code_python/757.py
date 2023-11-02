def solution():
    """Luna, the poodle, is supposed to eat 2 cups of kibble every day.  But Luna's master, Mary, and her husband, Frank, sometimes feed Luna too much kibble.  One day, starting with a new, 12-cup bag of kibble, Mary gave Luna 1 cup of kibble in the morning and 1 cup of kibble in the evening, But on the same day, Frank also gave Luna 1 cup of kibble in the afternoon and twice as much in the late evening as he had given Luna in the afternoon.  The next morning, how many cups of kibble will Mary find remaining in the bag?"""
    # Define the amount of kibble Luna is supposed to eat per day
    DAILY_KIBBLE = 2

    # Define the starting amount of kibble in the bag
    START_KIBBLE = 12

    # Calculate the amount of kibble Mary has fed Luna
    mary_kibble = 1 + 1

    # Calculate the amount of kibble Frank has fed Luna
    frank_kibble = 1 + (2 * 1)

    # Calculate the total amount of kibble Luna has eaten
    total_kibble = mary_kibble + frank_kibble

    # Calculate the amount of kibble remaining in the bag
    remaining_kibble = START_KIBBLE - total_kibble

    # Display the amount of kibble remaining in the bag
    result = remaining_kibble
    return result

print(solution())