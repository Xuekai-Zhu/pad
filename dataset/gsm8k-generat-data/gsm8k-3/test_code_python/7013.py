def solution():
    """Kevin's fish tank was leaking slowly at a rate of 1.5 ounces per hour.  He planned to go to the fish tank store later that day to get a new tank, but it may be as long as 12 hours before he can return home with the new tank.  Therefore, to collect the leaking fluid over that time, he placed a bucket underneath the tank that could hold twice the amount of fluid that would leak over 12 hours.  What size bucket, in ounces, did he use?"""
    # Define the rate of leaking and the time period
    rate = 1.5 # ounces/hour
    time_period = 12 # hours

    # Calculate the amount of fluid that will leak over the time period
    fluid_leak = rate * time_period # ounces

    # Calculate the size of the bucket needed
    bucket_size = fluid_leak * 2 # double the amount of fluid that will leak

    # Display the size of the bucket needed
    result = bucket_size
    return result

print(solution())