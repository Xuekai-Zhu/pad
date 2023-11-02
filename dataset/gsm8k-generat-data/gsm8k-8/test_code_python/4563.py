def solution():
    # Define the number of buckets of fish each animal is fed
    shark_buckets = 4
    dolphin_buckets = shark_buckets / 2
    other_buckets = shark_buckets * 5

    # Calculate the total number of buckets of fish used per day
    daily_buckets = shark_buckets + dolphin_buckets + other_buckets

    # Calculate the number of weeks 546 buckets will last
    weeks = 546 / daily_buckets / 7
    result = weeks
    return result

print(solution())