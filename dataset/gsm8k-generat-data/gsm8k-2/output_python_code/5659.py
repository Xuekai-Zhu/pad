def solution():
    """Mr. Willson worked on making his furniture for 3/4 an hour on Monday. On Tuesday, he worked for half an hour. Then he worked for 2/3 an hour on Wednesday and 5/6 of an hour on Thursday. If he worked for 75 minutes on Friday, how many hours in all did he work from Monday to Friday?"""
    monday_work = 3/4
    tuesday_work = 1/2
    wednesday_work = 2/3
    thursday_work = 5/6
    friday_work = 75/60   # convert minutes to hours
    
    total_work = monday_work + tuesday_work + wednesday_work + thursday_work + friday_work
    result = total_work
    return result

print(solution())