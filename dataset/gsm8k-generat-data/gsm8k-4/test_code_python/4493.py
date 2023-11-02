def solution():
    """Janet is getting paid to moderate social media posts. She gets paid 25 cents per post she checks. If it takes her 10 seconds to check a post, how much does she earn per hour?"""
    # Define the pay per post and the time to check each post
    pay_per_post = 0.25
    time_per_post = 10  # in seconds

    # Calculate the number of posts that can be checked in an hour
    posts_per_hour = 60 * 60 / time_per_post

    # Calculate the hourly pay
    hourly_pay = pay_per_post * posts_per_hour

    # Return the result
    result = hourly_pay
    return result

print(solution())