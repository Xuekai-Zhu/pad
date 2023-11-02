def solution():
    candies = 36 # Lisa has 36 candies
    eaten_candies = 0 # Initialize count of eaten candies
    days_weekly = 7 # There are 7 days in a week
    weeks = 0 # Initialize week counter

    while eaten_candies < candies:
        for day in range(days_weekly):
            if day == 0 or day == 2: # On Monday and Wednesday, she has 2 candies
                eaten_candies += 2
            else: # On other days, she has 1 candy
                eaten_candies += 1
        weeks += 1

    result = weeks
    return result

print(solution())