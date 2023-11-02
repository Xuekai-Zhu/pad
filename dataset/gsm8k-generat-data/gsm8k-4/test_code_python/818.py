def solution():
    """On Sunday Trey is going to do some chores at home. First, he wants to make a To Do list and count up how many things he has to do that day and how long it should take. He has several items under 'clean the house,' 'take a shower' and then 'make dinner.' In total there are 7 things to do to clean the house; 1 thing to do to take a shower; and 4 things to do to make dinner. If everything on Trey's list takes 10 minutes to do, how many hours total will it take to complete Trey's list?"""
    # Define the number of tasks for each chore
    clean_tasks = 7
    shower_tasks = 1
    dinner_tasks = 4

    # Define the time in minutes for each task
    task_time = 10

    # Calculate the total time in minutes
    total_time = (clean_tasks + shower_tasks + dinner_tasks) * task_time

    # Convert the total time to hours
    hours = total_time / 60

    # Round the result to two decimal places
    result = round(hours, 2)
    return result

print(solution())