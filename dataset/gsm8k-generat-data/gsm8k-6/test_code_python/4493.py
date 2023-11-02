def solution():
    # Calculate how many posts Janet can check in an hour (60 minutes = 3600 seconds)
    posts_per_hour = 3600 / 10  # each post takes 10 seconds to check

    # Calculate Janet's earnings per hour
    earnings_per_hour = posts_per_hour * 0.25  # she earns 25 cents per post checked

    result = earnings_per_hour
    return result

print(solution())