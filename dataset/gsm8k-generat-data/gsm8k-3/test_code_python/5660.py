def solution():
    """Mr. Willson worked on making his furniture for 3/4 an hour on Monday. On Tuesday, he worked for half an hour. Then he worked for 2/3 an hour on Wednesday and 5/6 of an hour on Thursday. If he worked for 75 minutes on Friday, how many hours in all did he work from Monday to Friday?"""
    # Calculate the total time worked in minutes
    total_minutes = (3/4 + 1/2 + 2/3 + 5/6 + 75/60) * 60

    # Convert to hours
    total_hours = total_minutes / 60

    # Display the total hours worked
    result = total_hours
    return result

print(solution())