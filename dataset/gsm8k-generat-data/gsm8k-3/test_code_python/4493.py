def solution():
    """Janet is getting paid to moderate social media posts. She gets paid 25 cents per post she checks. If it takes her 10 seconds to check a post, how much does she earn per hour?"""
    # Define the pay rate per post and the time it takes to check a post
    PAY_RATE = 0.25
    CHECK_TIME = 10  # in seconds

    # Convert check time to hours
    check_time_hours = CHECK_TIME / 3600

    # Calculate the pay rate per hour
    pay_rate_hour = PAY_RATE / check_time_hours

    # Display the pay rate per hour
    result = pay_rate_hour
    return result

print(solution())