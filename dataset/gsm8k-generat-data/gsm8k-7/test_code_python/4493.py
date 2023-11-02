def solution():
    pay_per_post = 0.25
    time_per_post = 10  # in seconds
    time_per_hour = 3600  # in seconds

    # Calculate the number of posts Janet can check in an hour
    posts_per_hour = time_per_hour / time_per_post

    # Calculate how much Janet earns per hour
    earnings_per_hour = pay_per_post * posts_per_hour
    result = earnings_per_hour
    return result

print(solution())