def solution():
    """On Sunday Trey is going to do some chores at home. First, he wants to make a To Do list and count up how many things he has to do that day and how long it should take. He has several items under 'clean the house,' 'take a shower' and then 'make dinner.' In total there are 7 things to do to clean the house; 1 thing to do to take a shower; and 4 things to do to make dinner. If everything on Trey's list takes 10 minutes to do, how many hours total will it take to complete Trey's list?"""
    total_tasks = 7 + 1 + 4
    task_time = 10 #in minutes
    total_time = total_tasks * task_time / 60 #convert to hours
    result = total_time
    return result

print(solution())