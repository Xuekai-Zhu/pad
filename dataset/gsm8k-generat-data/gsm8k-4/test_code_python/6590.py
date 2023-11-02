def solution():
    """Davida worked 35 hours on each of Weeks 1 and 2. She worked 48 hours each of Weeks 3 and 4. How many more hours did Davida work on Weeks 3 and 4 than on Weeks 1 and 2?"""
    # Define the number of hours worked in each week
    hours_week1 = 35
    hours_week2 = 35
    hours_week3 = 48
    hours_week4 = 48

    # Calculate the total number of hours worked in Weeks 1 and 2
    total_hours_1_2 = hours_week1 + hours_week2

    # Calculate the total number of hours worked in Weeks 3 and 4
    total_hours_3_4 = hours_week3 + hours_week4

    # Calculate the difference in hours worked between Weeks 3/4 and Weeks 1/2
    difference = total_hours_3_4 - total_hours_1_2

    result = difference
    return result

print(solution())