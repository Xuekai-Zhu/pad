def solution():
    """Every Sunday John is allowed to watch cartoons. However, for every 10 minutes of cartoons, he has to do 8 minutes of chores. If he watches cartoons for 2 hours, how many minutes of chores does he have to do?"""
    # Define the ratio of cartoons to chores
    CARTOON_RATIO = 10/8

    # Calculate the total number of minutes of cartoons watched
    cartoon_minutes = 2 * 60

    # Calculate the number of minutes of chores required
    chore_minutes = cartoon_minutes / CARTOON_RATIO

    # Display the number of minutes of chores required
    result = chore_minutes
    return result

print(solution())