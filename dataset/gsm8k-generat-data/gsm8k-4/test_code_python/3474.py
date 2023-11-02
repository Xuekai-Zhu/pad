def solution():
    """Heather helps her neighbour pick weeds out of her garden. She gets paid 5 cents for every weed she picks. On average, how many seconds can she take to pick a weed if she wants to earn $10 an hour?"""
    # Define the pay per weed and the target hourly pay
    PAY_PER_WEED = 0.05
    TARGET_PAY = 10

    # Calculate the number of weeds Heather needs to pick to earn the target pay
    weeds_needed = TARGET_PAY / (PAY_PER_WEED * 3600)

    # Calculate the average time, in seconds, Heather can take to pick a weed
    time_per_weed = 1 / weeds_needed

    # Return the result in seconds, rounded to the nearest integer
    result = round(time_per_weed)
    return result

print(solution())