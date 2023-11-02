def solution():
    """Heather helps her neighbour pick weeds out of her garden. She gets paid 5 cents for every weed she picks. On average, how many seconds can she take to pick a weed if she wants to earn $10 an hour?"""
    desired_hourly_pay = 10
    cents_per_weed = 5
    weeds_per_hour = (desired_hourly_pay * 100) / cents_per_weed
    seconds_per_weed = 60 * 60 / weeds_per_hour
    result = seconds_per_weed
    return result

print(solution())