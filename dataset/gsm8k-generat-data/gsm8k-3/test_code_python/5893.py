def solution():
    """Mary, Jess, and Christina want to decorate a party room with balloons. Each person inflates balloons at different speeds, and they only have 30 minutes to inflate as many balloons as possible. Mary inflates 10 balloons per minute, Jess inflates 7 balloons per minute and Christina came 15 minutes late and was the slowest one inflating 4 balloons per minute. How many balloons can they inflate before running out of time?"""
    # Define the time Mary and Jess have to inflate balloons
    TIME_MARY_JESS = 30

    # Define the time Christina has to inflate balloons
    TIME_CHRISTINA = 15

    # Define the number of balloons each person can inflate per minute
    BALLOONS_MARY = 10
    BALLOONS_JESS = 7
    BALLOONS_CHRISTINA = 4

    # Calculate the number of balloons Mary and Jess can inflate in TIME_MARY_JESS minutes
    balloons_mary_jess = (BALLOONS_MARY + BALLOONS_JESS) * TIME_MARY_JESS

    # Calculate the number of balloons Christina can inflate in TIME_CHRISTINA minutes
    balloons_christina = BALLOONS_CHRISTINA * TIME_CHRISTINA

    # Calculate the total number of balloons inflated
    total_balloons = balloons_mary_jess + balloons_christina

    # Display the total number of balloons inflated
    result = total_balloons
    return result

print(solution())