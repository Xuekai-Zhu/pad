def solution():
    
    # Define the time Peter exercised on Sunday and Monday
    sunday_time = 23
    monday_time = 16

    # Calculate the total time Peter exercised on Monday and Sunday combined
    combined_time = sunday_time + monday_time

    # Calculate the time Peter wants to exercise on Tuesday
    tuesday_time = combined_time * 2

    # Calculate the time Peter needs to exercise on Tuesday to reach his goal
    tuesday_time_needed = tuesday_time - goal

    # Display the time Peter needs to exercise on Tuesday
    result = tuesday_time_needed
    return result

print(solution())