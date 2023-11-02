def solution():
    """Davida worked 35 hours on each of Weeks 1 and 2. She worked 48 hours each of Weeks 3 and 4. How many more hours did Davida work on Weeks 3 and 4 than on Weeks 1 and 2?"""
    # Define the number of hours worked in Weeks 1 and 2
    hours_12 = 35 * 2

    # Define the number of hours worked in Weeks 3 and 4
    hours_34 = 48 * 2

    # Calculate the difference in hours worked between Weeks 3 and 4 and Weeks 1 and 2
    diff_hours = hours_34 - hours_12

    # Display the difference in hours worked
    result = diff_hours
    return result

print(solution())