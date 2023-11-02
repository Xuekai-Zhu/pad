def solution():
    """While at the lake, Cohen saw 300 fish-eater birds that had migrated into the area recently walking by the lake, eating the fish they had caught. The number of birds at the lake doubled on the second day and reduced by 200 on the third day. How many fish-eater birds did Cohen see in the three days?"""
    day1_birds = 300
    day2_birds = day1_birds * 2
    day3_birds = day2_birds - 200
    total_birds = day1_birds + day2_birds + day3_birds
    result = total_birds
    return result

print(solution())