def solution():
    """Madeline spends 18 hours a week in class. She spends 4 hours per day working on homework. She spends 8 hours per day sleeping. She works part-time 20 hours per week. How many hours left over does Madeline have?"""
    # Define the hours Madeline spends on various activities
    class_hours = 18
    homework_hours = 4 * 7 # 4 hours per day for 7 days
    sleep_hours = 8 * 7 # 8 hours per day for 7 days
    work_hours = 20

    # Calculate the total number of hours Madeline spends each week
    total_hours = class_hours + homework_hours + sleep_hours + work_hours

    # Calculate the number of hours Madeline has left over
    leftover_hours = 168 - total_hours # There are 168 hours in a week

    # Display the number of hours Madeline has left over
    result = leftover_hours
    return result

print(solution())