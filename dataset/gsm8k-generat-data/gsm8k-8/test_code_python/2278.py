def solution():
    # Calculate the total number of dogs per day
    total_dogs = 3 * (6 + (4-6)//2)

    # Calculate the number of 30-minute walks
    num_30_min_walks = total_dogs * 4

    # Calculate the number of 60-minute walks
    num_60_min_walks = 6 * 5

    # Calculate the total earnings per day
    total_earnings = (num_30_min_walks * 15) + (num_60_min_walks * 20)

    # Calculate the total earnings per week
    total_weekly_earnings = total_earnings * 5

    result = total_weekly_earnings
    return result

print(solution())