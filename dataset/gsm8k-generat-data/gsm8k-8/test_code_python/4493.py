def solution():
    # Define how long it takes to check one post in hours
    time_per_post = 10 / 3600

    # Define how much Janet earns per post
    earnings_per_post = 0.25

    # Calculate how many posts Janet can check in an hour
    posts_per_hour = 1 / time_per_post

    # Calculate how much Janet earns per hour
    earnings_per_hour = earnings_per_post * posts_per_hour

    result = earnings_per_hour
    return result

print(solution())