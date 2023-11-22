def solution():
    
    # Define the hourly rates and the number of hours worked
    HOURLY_RATE = 15
    HOURS_WORKED = [5, 5, 2]

    # Calculate the total earnings for Monday and Wednesday
    monday_earnings = 4 * HOURS_WORKED * HOURLY_RATE
    wednesday_earnings = 2 * HOURS_WORKED * HOURLY_RATE

    # Calculate the total earnings for the two days
    total_earnings = monday_earnings + wednesday_earnings

    # Display the total earnings
    result = total_earnings
    return result

print(solution())