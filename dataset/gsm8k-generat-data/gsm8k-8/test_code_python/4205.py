def solution():
    # Define the number of birds on the first day
    day1_birds = 300

    # Double the number of birds on the second day
    day2_birds = day1_birds * 2

    # Subtract 200 birds on the third day
    day3_birds = day2_birds - 200

    # Calculate the total number of birds seen in the three days
    total_birds = day1_birds + day2_birds + day3_birds
    result = total_birds
    return result

print(solution())