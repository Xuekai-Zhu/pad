def solution():
 
    time_to_work = 70
    time_to_work_by_Paula = time_to_work * (3/5)
    time_to_work_by_Luke = time_to_work - time_to_work_by_Paula
    time_home_by_bus = time_to_work
    time_home_by_bike = time_to_work_by_Luke * 5
    total_time = time_home_by_bus + time_to_work + time_home_by_bike
 
    result = total_time
 
    return result

print(solution())