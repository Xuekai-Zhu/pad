def solution():
    """Mr. Willson worked on making his furniture for 3/4 an hour on Monday.
    On Tuesday, he worked for half an hour. Then he worked for 2/3 an hour on Wednesday
    and 5/6 of an hour on Thursday. If he worked for 75 minutes on Friday, how many
    hours in all did he work from Monday to Friday?"""
    monday_hours = 3 / 4
    tuesday_hours = 1 / 2
    wednesday_hours = 2 / 3
    thursday_hours = 5 / 6
    friday_hours = 75 / 60
    
    total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours + friday_hours
    result = total_hours
    
    return result

print(solution())