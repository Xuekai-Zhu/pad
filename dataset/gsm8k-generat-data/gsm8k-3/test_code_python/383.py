def solution():
    """On Monday, Matt worked for 450 minutes in his office.  On Tuesday, he worked half the number of minutes he worked on Monday.  On Wednesday, he worked for 300 minutes.  How many more minutes did he work on Wednesday than on Tuesday."""
    # Define the number of minutes Matt worked on Monday, Tuesday, and Wednesday
    monday_minutes = 450
    tuesday_minutes = monday_minutes / 2
    wednesday_minutes = 300

    # Calculate the difference between the number of minutes Matt worked on Wednesday and Tuesday
    difference = wednesday_minutes - tuesday_minutes

    # Display the difference
    result = difference
    return result

print(solution())