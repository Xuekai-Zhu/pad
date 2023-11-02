def solution():
    """Heather helps her neighbour pick weeds out of her garden. She gets paid 5 cents for every weed she picks. On average, how many seconds can she take to pick a weed if she wants to earn $10 an hour?"""
    # Define the pay per weed and the desired hourly wage
    PAY_PER_WEED = 0.05
    DESIRED_HOURLY_WAGE = 10.00

    # Calculate the pay per second
    pay_per_second = DESIRED_HOURLY_WAGE / 3600

    # Calculate the maximum time in seconds to pick a weed
    max_time_per_weed = pay_per_second / PAY_PER_WEED

    # Display the maximum time in seconds to pick a weed
    result = max_time_per_weed
    return result

print(solution())