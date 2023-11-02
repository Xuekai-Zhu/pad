def solution():
    birdseed_capacity = 2  # in cups
    birdseed_per_week = 2  # in cups, emptied feeder refilled every week
    birdseed_available = birdseed_capacity - 0.5  # squirrel steals half a cup of birdseed
    birds_fed_per_cup = 14

    # Calculate the total number of birds fed per week
    birds_fed_per_week = birds_fed_per_cup * birdseed_available

    result = birds_fed_per_week
    return result

print(solution())