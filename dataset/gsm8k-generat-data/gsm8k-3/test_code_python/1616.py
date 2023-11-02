def solution():
    """It’s exam season and Tristan has several exams to prepare for. On Monday, he studies for 4 hours then studies for twice this long on Tuesday. On Wednesday, Thursday, and Friday he studies for 3 hours each day. He wants to study for a total of 25 hours over the week and divides the remaining amount of study time evenly between Saturday and Sunday. How many hours does Tristan spend studying on Saturday?"""
    # Define the number of hours Tristan studies on Monday
    monday_hours = 4

    # Define the number of hours Tristan studies on Tuesday
    tuesday_hours = 2 * monday_hours

    # Define the number of hours Tristan studies on Wednesday, Thursday, and Friday
    weekday_hours = 3 * 3

    # Define the total number of hours Tristan wants to study for the week
    total_hours = 25

    # Calculate the total number of hours Tristan has already studied
    already_studied = monday_hours + tuesday_hours + weekday_hours

    # Calculate the remaining number of study hours Tristan needs to reach his goal
    remaining_hours = total_hours - already_studied

    # Divide the remaining hours evenly between Saturday and Sunday
    saturday_hours = remaining_hours / 2

    # Display the number of hours Tristan spends studying on Saturday
    result = saturday_hours
    return result

print(solution())