def solution():
    """On Sunday Trey is going to do some chores at home. First, he wants to make a To Do list and count up how many things he has to do that day and how long it should take. He has several items under 'clean the house,' 'take a shower' and then 'make dinner.' In total there are 7 things to do to clean the house; 1 thing to do to take a shower; and 4 things to do to make dinner. If everything on Trey's list takes 10 minutes to do, how many hours total will it take to complete Trey's list?"""
    # Define the number of tasks and the time per task
    CLEANING_TASKS = 7
    SHOWER_TASKS = 1
    DINNER_TASKS = 4
    TIME_PER_TASK = 10 # in minutes

    # Calculate the total time in minutes
    total_time = (CLEANING_TASKS + SHOWER_TASKS + DINNER_TASKS) * TIME_PER_TASK

    # Convert the total time to hours and round to 2 decimal places
    total_time_hours = round(total_time / 60, 2)

    # Display the total time in hours
    result = total_time_hours
    return result

print(solution())