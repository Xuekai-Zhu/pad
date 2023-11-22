def solution():
    
    # Define the number of miles Pancho walks per day and the number of days in a week
    daily_distance = 20
    weekend_distance = 10
    days_in_week = 7

    # Calculate the total distance Pancho walks in a week
    total_distance = (daily_distance * days_in_week) + (weekend_distance * 2)

    # Display the total distance
    result = total_distance
    return result

print(solution())