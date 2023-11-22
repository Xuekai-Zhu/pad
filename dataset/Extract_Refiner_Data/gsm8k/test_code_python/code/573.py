def solution():
    
    # Define the number of birds seen on each day
    day1 = 50
    day2 = 50
    day3 = 0
    day4 = 120
    day5 = 120
    day6 = 20
    day7 = 90

    # Calculate the total number of birds seen over the next week
    total_birds = day1 + day2 + day3 + day4 + day5 + day6 + day7

    # Calculate the average number of birds seen per day
    avg_birds_per_day = total_birds / 7

    # Display the average number of birds seen per day
    result = avg_birds_per_day
    return result

print(solution())