def solution():
    # Calculate the number of weeds Heather needs to pick in an hour to earn $10
    weeds_per_hour = 10 / 0.05  # Heather earns 5 cents for every weed she picks

    # Calculate the number of seconds Heather can take to pick one weed
    seconds_per_weed = 3600 / weeds_per_hour  # there are 3600 seconds in an hour

    result = seconds_per_weed
    return result

print(solution())