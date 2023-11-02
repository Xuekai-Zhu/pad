def solution():
    """Mr. Willson worked on making his furniture for 3/4 an hour on Monday. On Tuesday, he worked for half an hour. Then he worked for 2/3 an hour on Wednesday and 5/6 of an hour on Thursday. If he worked for 75 minutes on Friday, how many hours in all did he work from Monday to Friday?"""
    # Define the times worked on each day in fractions of an hour
    monday_time = 3/4
    tuesday_time = 1/2
    wednesday_time = 2/3
    thursday_time = 5/6
    friday_time = 75/60

    # Add up the times worked on each day to find the total time worked
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time + friday_time

    # Convert the total time worked to hours and round to two decimal places
    hours_worked = round(total_time, 2)

    # return the result
    result = hours_worked
    return result

print(solution())