def solution():
    posts_per_hour = 3600 / 10  # Janet can check 3600 seconds of posts in an hour (60 minutes * 60 seconds)
    earnings_per_hour = posts_per_hour * 0.25  # Janet earns 25 cents per post checked

    result = earnings_per_hour
    return result

print(solution())