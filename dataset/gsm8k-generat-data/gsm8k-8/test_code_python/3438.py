def solution():
    # Define the total number of days
    total_days = 5

    # Define the first day's earnings
    day_1_earnings = 10

    # Define the earnings increase per day
    daily_increase = 4

    # Calculate the total earnings
    total_earnings = day_1_earnings + daily_increase*(total_days-1)

    result = total_earnings
    return result

print(solution())