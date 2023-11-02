def solution():
    """A cat spends its time hunting birds. The cat catches 8 birds during the day and twice this many at night. In total, how many birds did the cat catch?"""
    # Define the number of birds caught during the day
    birds_day = 8

    # Define the number of birds caught at night
    birds_night = birds_day * 2

    # Calculate the total number of birds caught
    total_birds = birds_day + birds_night

    # Display the total number of birds caught
    result = total_birds
    return result

print(solution())