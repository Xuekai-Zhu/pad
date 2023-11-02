def solution():
    walk_time = 10
    train_time = 80
    travel_time = walk_time + train_time
    leave_time = 900 - travel_time
    result = leave_time
    
    return result

print(solution())