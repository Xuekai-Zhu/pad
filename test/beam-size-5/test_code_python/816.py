def solution():
    
    # Define the number of hours Sandy walked on the first day
    day1_hours = 8

    # Define the number of hours Sandy walked on the second day
    day2_hours = day1_hours / 2

    # Calculate the total number of hours Sandy walked in two days
    total_hours = day1_hours + day2_hours + day3_hours

    # Convert the total hours to minutes
    total_minutes = total_hours * 60

    # return the result
    result = total_minutes
    return result

print(solution())