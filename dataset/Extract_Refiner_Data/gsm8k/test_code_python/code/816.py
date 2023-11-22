def solution():
    
    # Define the number of hours Sandy walked on the first day
    first_day_hours = 8

    # Define the number of hours Sandy walked on the second day
    second_day_hours = first_day_hours / 2

    # Calculate the total number of hours Sandy walked in two days
    total_hours = first_day_hours + second_day_hours

    # Convert the total hours to minutes
    total_minutes = total_hours * 60

    # Display the total time in minutes
    result = total_minutes
    return result

print(solution())