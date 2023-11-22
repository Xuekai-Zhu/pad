def solution():
    
    # Define the number of hours Sadie slept on Monday
    monday_hours = 8

    # Define the number of hours Sadie slept on the next two days
    next_two_days_hours = 2 * monday_hours - 2

    # Define the number of hours Sadie slept on the rest of the week
    rest_of_week_hours = next_two_days_hours + 1

    # Calculate the total number of hours Sadie slept in the week
    total_hours = monday_hours + next_two_days_hours + rest_of_week_hours

    # Display the total number of hours Sadie slept
    result = total_hours
    return result

print(solution())