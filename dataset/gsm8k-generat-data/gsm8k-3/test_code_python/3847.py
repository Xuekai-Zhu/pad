def solution():
    """If a crowd contains 24 people named Barry, 20 people named Kevin, 80 people named Julie, and 50 people named Joe, how many nice people are in the crowd?"""
    # Define the percentage of people with each name that are nice
    BARRY_NICE_PERCENTAGE = 100
    KEVIN_NICE_PERCENTAGE = 50
    JULIE_NICE_PERCENTAGE = 75
    JOE_NICE_PERCENTAGE = 10

    # Calculate the number of nice people with each name
    barry_nice = int(24 * (BARRY_NICE_PERCENTAGE / 100))
    kevin_nice = int(20 * (KEVIN_NICE_PERCENTAGE / 100))
    julie_nice = int(80 * (JULIE_NICE_PERCENTAGE / 100))
    joe_nice = int(50 * (JOE_NICE_PERCENTAGE / 100))

    # Calculate the total number of nice people
    total_nice = barry_nice + kevin_nice + julie_nice + joe_nice

    # Display the total number of nice people
    result = total_nice
    return result

print(solution())