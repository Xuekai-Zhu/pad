def solution():
    
    # Define the amount of butter needed to make 1 dozen croissants
    BUTTER_PER_DOZEN = 0.25

    # Define the number of dozens of croissants Juan wants to make per day
    dozens_per_day = 4

    # Calculate the total amount of butter needed for a day of croissants
    butter_per_day = dozens_per_day * BUTTER_PER_DOZEN

    # Calculate the total amount of butter needed for a week of croissants
    butter_per_week = butter_per_day * 7

    # Display the total amount of butter needed
    result = butter_per_week
    return result

print(solution())