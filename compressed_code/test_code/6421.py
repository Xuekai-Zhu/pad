def solution():
    
    clean_house = 7
    take_shower = 1
    make_dinner = 4
    total_tasks = clean_house + take_shower + make_dinner
    time_per_task = 10 
    total_time = total_tasks * time_per_task 
    hours = total_time / 60 
    result = hours
    return result

print(solution())