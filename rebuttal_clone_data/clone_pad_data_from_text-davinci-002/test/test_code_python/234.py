def solution():
    minutes_laundry = 30
    minutes_bathroom = 15
    minutes_homework = 40
    total_time = 2 * 60 #2 hours in minutes
    room_cleaning_time = total_time - minutes_laundry - minutes_bathroom - minutes_homework
    result = room_cleaning_time
    
    return result

print(solution())