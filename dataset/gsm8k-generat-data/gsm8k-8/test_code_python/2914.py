def solution():
    # Calculate the total grams of birdseed Leah has
    total_seed = (3 + 5) * 225

    # Calculate the total grams of birdseed the birds eat in a week
    total_eaten = 100 + 50

    # Calculate the number of weeks Leah can feed her birds without going back to the store
    weeks_of_feed = total_seed / total_eaten
    result = weeks_of_feed
    return result

print(solution())