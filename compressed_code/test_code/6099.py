def solution():
    
    total_time = 2 * 60  
    laundry_time = 30
    bathroom_time = 15
    homework_time = 40
    room_time = total_time - laundry_time - bathroom_time - homework_time
    result = room_time
    return result

print(solution())