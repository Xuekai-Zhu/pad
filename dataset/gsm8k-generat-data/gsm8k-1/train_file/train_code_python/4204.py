def solution():
    """While at the lake, Cohen saw 300 fish-eater birds that had migrated into the area recently walking by the lake, eating the fish they had caught. The number of birds at the lake doubled on the second day and reduced by 200 on the third day. How many fish-eater birds did Cohen see in the three days?"""
    birds_on_day_one = 300
    birds_on_day_two = birds_on_day_one * 2
    birds_on_day_three = birds_on_day_two - 200
    total_birds = birds_on_day_one + birds_on_day_two + birds_on_day_three
    result = total_birds
    return result

print(solution())