def solution():
    """On Sunday Trey is going to do some chores at home. First, he wants to make a To Do list and count up how many things he has to do that day and how long it should take. He has several items under 'clean the house,' 'take a shower' and then 'make dinner.' In total there are 7 things to do to clean the house; 1 thing to do to take a shower; and 4 things to do to make dinner. If everything on Trey's list takes 10 minutes to do, how many hours total will it take to complete Trey's list?"""
    clean_house = 7
    take_shower = 1
    make_dinner = 4
    total_tasks = clean_house + take_shower + make_dinner
    time_per_task = 10 # minutes
    total_time = total_tasks * time_per_task # minutes
    hours = total_time / 60 # convert to hours
    result = hours
    return result

print(solution())