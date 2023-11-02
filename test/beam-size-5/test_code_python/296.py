def solution():
    
    # Define the number of minutes Peter exercised on Sunday
    sunday_minutes = 23

    # Define the number of minutes Peter exercised on Monday
    monday_minutes = 16

    # Calculate the combined number of minutes Peter exercised
    combined_minutes = sunday_minutes + monday_minutes

    # Calculate the number of minutes Peter needs to exercise on Tuesday to reach his goal
    tuesday_minutes = 2 * combined_minutes

    # Display the number of minutes Peter needs to exercise on Tuesday
    result = tuesday_minutes
    return result

print(solution())