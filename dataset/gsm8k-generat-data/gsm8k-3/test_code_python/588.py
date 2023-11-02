def solution():
    """John worked 8 hours a day every day from the 3rd to the 8th, including the 3rd and not including the 8th.  How many hours did he work?"""
    # Calculate the number of days John worked
    days_worked = 8 - 3

    # Calculate the total number of hours John worked
    total_hours = days_worked * 8

    # Display the total number of hours John worked
    result = total_hours
    return result

print(solution())