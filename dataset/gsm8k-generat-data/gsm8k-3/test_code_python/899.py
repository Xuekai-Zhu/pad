def solution():
    """Ben works 8-hour shifts in a furniture shop.  It takes him 5 hours to build 1 rocking chair.  How many chairs can he build in 10 days?"""
    # Define the number of hours Ben works per day
    WORK_HOURS_PER_DAY = 8

    # Define the number of hours it takes Ben to build 1 rocking chair
    CHAIR_BUILD_TIME = 5

    # Calculate the number of chairs Ben can build per day
    chairs_per_day = WORK_HOURS_PER_DAY / CHAIR_BUILD_TIME

    # Calculate the total number of chairs Ben can build in 10 days
    total_chairs = chairs_per_day * 10

    # Display the total number of chairs
    result = total_chairs
    return result

print(solution())