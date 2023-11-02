def solution():
    """Heather helps her neighbour pick weeds out of her garden. She gets paid 5 cents for every weed she picks. On average, how many seconds can she take to pick a weed if she wants to earn $10 an hour?"""
    weeds_per_hour = (10 * 100) / 5  # converting dollars to cents and dividing by the pay per weed
    seconds_per_hour = 60 * 60
    seconds_per_weed = seconds_per_hour / weeds_per_hour
    result = seconds_per_weed
    return result

print(solution())