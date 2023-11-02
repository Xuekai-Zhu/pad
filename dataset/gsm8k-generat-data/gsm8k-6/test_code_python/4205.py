def solution():
    # Calculate the total number of fish-eater birds seen by Cohen in three days
    day1_birds = 300
    day2_birds = day1_birds * 2  # number of birds doubled on the second day
    day3_birds = day2_birds - 200  # number of birds reduced by 200 on the third day
    total_birds = day1_birds + day2_birds + day3_birds  # total number of birds in the three days
    result = total_birds
    return result

print(solution())